message(STATUS "Making interface metal-cpp-extensions library")
add_library(metal-cpp-extensions INTERFACE)
target_include_directories(metal-cpp-extensions INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}/include")