cmake_minimum_required(VERSION 3.9)
project(moodycamel VERSION 1.0.0)

include(GNUInstallDirs)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(moodycamel INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)

