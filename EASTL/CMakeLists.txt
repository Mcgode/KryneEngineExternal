
cmake_minimum_required(VERSION 3.10)

# We will be manually linking libs from subdirectories, allow it
cmake_policy(SET CMP0079 NEW)

message(STATUS "Setting up EASTL")

set(EASTL_ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

set(EASTL_DIR "eastl-3.27.01")
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_CURRENT_SOURCE_DIR}/${EASTL_DIR}/scripts/CMake")

add_subdirectory(eabase-0699a15)

add_subdirectory(eaassert-e5e1812)
add_subdirectory(eathread-a77e227)

add_subdirectory(eastdc-fbcc34e)

target_link_libraries(EAStdC EAAssert)

set(EASTL_DISABLE_APRIL_2024_DEPRECATIONS ON)
set(EASTL_DISABLE_SEPT_2024_DEPRECATIONS ON)
set(EASTL_DISABLE_APRIL_2025_DEPRECATIONS ON)
add_subdirectory(${EASTL_DIR})

target_link_libraries(EASTL EAStdC)