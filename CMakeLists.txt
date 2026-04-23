
#Set up EASTL
add_subdirectory(EASTL)
set_target_properties(EABase PROPERTIES Type "External")
set_target_properties(EABase PROPERTIES FOLDER "External")
set_target_properties(EASTL PROPERTIES Type "External")
set_target_properties(EASTL PROPERTIES FOLDER "External")


# Set up GLFW3
set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_INSTALL OFF CACHE BOOL "" FORCE)
set(USE_MSVC_RUNTIME_LIBRARY_DLL OFF CACHE BOOL "" FORCE)
add_subdirectory(glfw)

set_target_properties(glfw PROPERTIES Type "External")
#SetTargetFlags(glfw)
set_target_properties(glfw PROPERTIES FOLDER "External")
set_target_properties(update_mappings PROPERTIES FOLDER "External")


# Set up ImGui
add_subdirectory(imgui)
set_target_properties(DearImgui PROPERTIES FOLDER "External")


#Set up moody camel libs
add_subdirectory(moodycamel)
set_target_properties(moodycamel PROPERTIES FOLDER "External")


# Set up glm
add_subdirectory(glm)


# Set up DirectX hedears lib
if (GraphicsApi STREQUAL "DX12")
    add_subdirectory(DirectX-Headers)
    set_target_properties(DirectX-Headers PROPERTIES FOLDER "External")
    set_target_properties(DirectX-Guids PROPERTIES FOLDER "External")
endif ()


# Set up DX12MemoryAllocator
if (GraphicsApi STREQUAL "DX12")
    add_subdirectory(DirectX12MemoryAllocator)
    set_target_properties(D3D12MemoryAllocator PROPERTIES FOLDER "External")
endif ()

# Set up VulkanMemoryAllocator
if (GraphicsApi STREQUAL "VK")
    add_subdirectory(VulkanMemoryAllocator)
    set_target_properties(VulkanMemoryAllocator PROPERTIES FOLDER "External")
endif ()

# Set up tracy
set(TRACY_ENABLE ON CACHE BOOL "Enable tracy" FORCE)
set(TRACY_FIBERS ON CACHE BOOL "Enable tracy fibers" FORCE)
add_subdirectory(tracy-0.13.1)
set_target_properties(TracyClient PROPERTIES FOLDER "External")

# Set up Google Test
set(INSTALL_GTEST OFF CACHE BOOL "Install GTest" FORCE)
add_subdirectory(googletest)
set_target_properties(gtest PROPERTIES FOLDER "External")
set_target_properties(gtest_main PROPERTIES FOLDER "External")
set_target_properties(gmock PROPERTIES FOLDER "External")
set_target_properties(gmock_main PROPERTIES FOLDER "External")

# Set up boost
add_subdirectory(boost)
set_target_properties(boost_context PROPERTIES FOLDER "External")

if (GraphicsApi STREQUAL "MTL")
    add_subdirectory(metal-cpp)
    add_subdirectory(metal-cpp-extensions)
endif ()

#Set up WinPixEventRuntime
add_subdirectory(WinPixEventRuntime)

# Set up zstd lib
add_subdirectory(zstd-1.5.7)
