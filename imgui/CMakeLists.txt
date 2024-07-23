
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

set(ImGuiDx12Src
        backends/imgui_impl_glfw.cpp backends/imgui_impl_glfw.h
        backends/imgui_impl_dx12.cpp backends/imgui_impl_dx12.h)

add_library(DearImgui STATIC ${ImGuiBaseSrc})
target_include_directories(DearImgui PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_property(TARGET DearImgui PROPERTY Type "External")

add_library(DearImguiVk STATIC ${ImGuiVkSrc})
target_include_directories(DearImguiVk PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_property(TARGET DearImguiVk PROPERTY Type "External")

add_library(DearImguiDx12 STATIC ${ImGuiDx12Src})
target_include_directories(DearImguiDx12 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_property(TARGET DearImguiDx12 PROPERTY Type "External")

target_link_libraries(DearImguiVk DearImgui glfw)
target_link_libraries(DearImguiDx12 DearImgui glfw)

#SetTargetFlags(DearIMGUI)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}")