
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

add_library(DearImgui STATIC ${ImGuiBaseSrc})
target_include_directories(DearImgui PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_property(TARGET DearImgui PROPERTY Type "External")

#SetTargetFlags(DearIMGUI)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}")