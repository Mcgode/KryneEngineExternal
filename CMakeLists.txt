
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

set_target_properties(EAStdC PROPERTIES FOLDER "External")
set_target_properties(EAAssert PROPERTIES FOLDER "External")
set_target_properties(EAThread PROPERTIES FOLDER "External")
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

# Set up xsimd
add_subdirectory(xsimd)

# Set up Assimp
set(BUILD_SHARED_LIBS OFF CACHE BOOL "Build package with shared libraries." FORCE)
set(ASSIMP_BUILD_TESTS OFF CACHE BOOL "If the test suite for Assimp is built in addition to the library." FORCE)
set(ASSIMP_INSTALL OFF CACHE BOOL "Disable this if you want to use assimp as a submodule." FORCE)
add_subdirectory(assimp-5.4.3)
set_target_properties(assimp PROPERTIES FOLDER "External")
if (TARGET UpdateAssimpLibsDebugSymbolsAndDLLs)
    set_target_properties(UpdateAssimpLibsDebugSymbolsAndDLLs PROPERTIES FOLDER "External")
endif ()
if (TARGET zlibstatic)
    set_target_properties(zlibstatic PROPERTIES FOLDER "External")
endif ()

#Set up WinPixEventRuntime
add_subdirectory(WinPixEventRuntime)