
#Set up EASTL
set(EASTL_ROOT_DIR "${PROJECT_SOURCE_DIR}/external-libs/eastl")

message(STATUS "Setting up EASTL")

set(EASTL_INCLUDE_DIRS
        "${EASTL_ROOT_DIR}/test/packages/EAAssert/include"
        "${EASTL_ROOT_DIR}/test/packages/EABase/include/Common"
        "${EASTL_ROOT_DIR}/test/packages/EAMain/include"
        "${EASTL_ROOT_DIR}/test/packages/EAStdC/include"
        "${EASTL_ROOT_DIR}/test/packages/EATest/include"
        "${EASTL_ROOT_DIR}/test/packages/EAThread/include")
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_CURRENT_SOURCE_DIR}/eastl/scripts/CMake")

add_subdirectory(./eastl)
set_property(TARGET EASTL PROPERTY Type "External")
#SetTargetFlags(EASTL)

add_subdirectory(./eastl/test/packages/EAAssert)
set_property(TARGET EAAssert PROPERTY Type "External")
target_include_directories(EAAssert PUBLIC ${EASTL_INCLUDE_DIRS})
#SetTargetFlags(EAAssert)

add_subdirectory(./eastl/test/packages/EAThread)
set_property(TARGET EAThread PROPERTY Type "External")
target_include_directories(EAThread PUBLIC ${EASTL_INCLUDE_DIRS})
#SetTargetFlags(EAThread)

add_subdirectory(./eastl/test/packages/EAStdC)
set_property(TARGET EAStdC PROPERTY Type "External")
target_include_directories(EAStdC PUBLIC ${EASTL_INCLUDE_DIRS})
#SetTargetFlags(EAStdC)

target_link_libraries(EASTL EAStdC EAAssert EAThread)


# Set up GLFW3
set(BUILD_SHARED_LIBS OFF)
set(USE_MSVC_RUNTIME_LIBRARY_DLL OFF)
add_subdirectory(glfw)

set_target_properties(glfw PROPERTIES Type "External")
#SetTargetFlags(glfw)


# Set up ImGui
add_subdirectory(imgui)


#Set up moody camel libs
add_subdirectory(moodycamel)


# Set up glm
add_subdirectory(glm)


# Set up DirectX hedears lib
add_subdirectory(DirectX-Headers)


# Set up RenderPipelineshaders
set(RpsBuildExamples OFF)
set(RpsBuildTests OFF)
set(RpsBuildTools OFF)
add_subdirectory(RenderPipelineShaders)
target_include_directories(rps_runtime_vk PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/RenderPipelineShaders/include")
target_include_directories(rps_runtime_d3d12 PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/RenderPipelineShaders/include")