message(STATUS "Making interface MetalCpp library")
add_library(MetalCpp INTERFACE include/Metal/Metal.hpp)
target_include_directories(MetalCpp INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}/include")