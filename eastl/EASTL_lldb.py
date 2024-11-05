import lldb

def __lldb_init_module(debugger, internal_dict):
    def addSummary(type_name, summary_name, templated=True):
        command = None
        if templated:
            command = f'type summary add -x "^{type_name}(( )?&)?$" -F {__name__}.{summary_name} -w eastl'
        else:
            command = f'type synthetic add {type_name} -F {__name__}.{summary_name} -w eastl'
        debugger.HandleCommand(command)

    def addSytheticChildrenProvider(type_name, provider_name, templated=True):
        command = None
        if templated:
            command = f'type synthetic add -x "^{type_name}(( )?&)?$" --python-class {__name__}.{provider_name} -w eastl'
        else:
            command = f'type synthetic add {type_name} --python-class {__name__}.{provider_name} -w eastl'
        debugger.HandleCommand(command)

    addSummary("eastl::unique_ptr<.*>", unique_ptr_summary.__name__)
    addSytheticChildrenProvider("eastl::unique_ptr<.*>", UniquePtrChildrenProvider.__name__)

    addSummary("eastl::basic_string<.*>", basic_string_summary.__name__)
    addSytheticChildrenProvider("eastl::basic_string<.*>", BasicStringChildrenProvider.__name__)

    addSummary("eastl::VectorBase<.*>", vector_base_summary.__name__)
    addSytheticChildrenProvider("eastl::VectorBase<.*>", VectorBaseChildrenProvider.__name__)
    addSummary("eastl::vector<.*>", vector_base_summary.__name__)
    addSytheticChildrenProvider("eastl::vector<.*>", VectorBaseChildrenProvider.__name__)
    addSummary("eastl::fixed_vector<.*>", vector_base_summary.__name__)
    addSytheticChildrenProvider("eastl::fixed_vector<.*>", VectorBaseChildrenProvider.__name__)

    debugger.HandleCommand("type category enable eastl")

def unique_ptr_summary(value_object, internal_dict):
    data_ptr = value_object.GetChildMemberWithName("[pointer]")
    if data_ptr.GetValueAsUnsigned() == 0:
        return "{ nullptr }"
    else:
        return f'{{ {data_ptr.GetValueAsUnsigned():#x} }}'

class UniquePtrChildrenProvider:
    def __init__(self, value_object, internal_dict):
        self.value_object = value_object
        self.data_ptr = None
        self.value_type = None

    def update(self):
        self.data_ptr = self.value_object.GetChildMemberWithName("mPair").GetChildMemberWithName("mFirst")

    def num_children(self):
        return 2

    def get_child_index(self, name):
        if name == "[value]":
            return 1
        else:
            return 0

    def get_child_at_index(self, index):
        if index == 0:
            return self.data_ptr.Clone("[pointer]")
        if index == 1:
            return self.data_ptr.Dereference().Clone("[value]")

def basic_string_summary(value_object, internal_dict):
    return value_object.GetChildMemberWithName("[value]").GetSummary()

class BasicStringChildrenProvider:
    def __init__(self, value_object, internal_dict):
        self.value_object = value_object
        self.uses_heap = False

        # self.sso_capacity = lldb.frame.EvaluateExpression("eastl::basic_string<char, eastl::allocator>::SSOLayout::SSO_CAPACITY").GetValueAsUnsigned()

        self.update()

    def update(self):
        pair_first = self.value_object.GetChildMemberWithName("mPair").GetChildMemberWithName("mFirst")
        self.uses_heap = pair_first.EvaluateExpression("IsHeap()").GetValueAsUnsigned() == 1
        print("Uses heap: " + str(self.uses_heap))
        self.data_ptr = self.value_object.GetChildMemberWithName("mPair").GetChildMemberWithName("mFirst")

    def num_children(self):
        return 3

    def get_child_index(self, name):
        if name == "[length]":
            return 0
        elif name == "[capacity]":
            return 1
        else:
            return 2

    def get_child_at_index(self, index):
        if index == 0:
            return self.value_object.EvaluateExpression("size()").Clone("[length]")
        if index == 1:
            return self.value_object.EvaluateExpression("capacity()").Clone("[capacity]")
        if index == 2:
            return self.value_object.EvaluateExpression("c_str()").Clone("[value]")

def vector_base_summary(value_object, internal_dict):
    count = value_object.GetChildMemberWithName("[size]").GetValueAsUnsigned()
    if count == 0:
        return f'[{count}] {{}}'
    values = [value_object.GetChildMemberWithName(f'[{i}]') for i in range(min(count, 6))]
    if values[0].GetSummary() is not None:
        values = [value.GetSummary() for value in values]
    elif values[0].GetValue() is not None:
        values = [value.GetValue() for value in values]
    else:
        values = [f"{value.GetType().GetName()}{{...}}" for value in values]
    print(values)
    values_str = ", ".join(values)
    if count > 6:
        return f'[{count}] {{ {values_str},... }}'
    else:
        return f'[{count}] {{ {values_str} }}'

class VectorBaseChildrenProvider:
    def __init__(self, value_object, internal_dict):
        self.value_object = value_object
        self.mp_begin = None
        self.mp_end = None
        self.count = 0
        self.data_type = None
        self.data_size = None
        self.update()

    def update(self):
        self.mp_begin = self.value_object.GetChildMemberWithName("mpBegin")
        self.count = self.value_object.EvaluateExpression("mpEnd-mpBegin").GetValueAsUnsigned()

        self.data_type = self.value_object.GetType().GetTemplateArgumentType(0)
        self.data_size = self.data_type.GetByteSize()

    def num_children(self):
        return 2 + self.count

    def get_child_index(self, name):
        if name == "[size]":
            return 0
        elif name == "[capacity]":
            return 1
        else:
            try:
                return int(name.lstrip('[').rstrip(']')) + 2
            except:
                return -1

    def get_child_at_index(self, index):
        if index == 0:
            return self.value_object.EvaluateExpression("mpEnd - mpBegin").Clone("[size]")
        elif index == 1:
            return self.value_object.EvaluateExpression("mCapacityAllocator.mFirst - mpBegin").Clone("[capacity]")
        else:
            offset = self.data_size * (index - 2)
            return self.mp_begin.CreateChildAtOffset(f"[{index - 2}]", offset, self.data_type)