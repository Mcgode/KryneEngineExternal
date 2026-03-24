
add_library(libzstd STATIC zstd.h zdict.h zstd_errors.h zstd.c)
target_include_directories(libzstd PUBLIC ./)
set_target_properties(libzstd PROPERTIES FOLDER "External")