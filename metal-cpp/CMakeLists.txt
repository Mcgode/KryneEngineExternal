message(STATUS "Making interface metal-cpp library")
add_library(metal-cpp INTERFACE)
target_include_directories(metal-cpp INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}/include")