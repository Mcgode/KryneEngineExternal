
set(ImGuiBaseSrc
        imconfig.h
        imgui.cpp imgui.h
        imgui_demo.cpp
        imgui_draw.cpp
        imgui_internal.h
        imgui_tables.cpp
        imgui_widgets.cpp
        imstb_rectpack.h
        imstb_textedit.h
        imstb_truetype.h)

set(ImGuiVkSrc
        backends/imgui_impl_glfw.cpp backends/imgui_impl_glfw.h
        backends/imgui_impl_vulkan.cpp backends/imgui_impl_vulkan.h)

set(ImGuiVkSrc
        backends/imgui_impl_glfw.cpp backends/imgui_impl_glfw.h
        backends/imgui_impl_dx12.cpp backends/imgui_impl_dx12.h)

if (GraphicsApi STREQUAL "VK")
    set(ImGuiSrc ${ImGuiBaseSrc} ${ImGuiVkSrc})
elseif (GraphicsApi STREQUAL "DX12")
    set(ImGuiSrc ${ImGuiBaseSrc} ${ImGuiDx12Src})
endif()

add_library(DearIMGUI STATIC ${ImGuiSrc})

target_link_libraries(DearIMGUI glfw)

set_property(TARGET DearIMGUI PROPERTY Type "External")
#SetTargetFlags(DearIMGUI)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}")