message(STATUS "Making interface MetalCpp library")
add_library(MetalCpp INTERFACE)
target_include_directories(MetalCpp INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}/include")