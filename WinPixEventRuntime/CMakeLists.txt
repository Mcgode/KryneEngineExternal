project(WinPixEventRuntime)

if (WIN32)
    if (SYSTEM_PROCESSOR MATCHES "amd64" OR SYSTEM_PROCESSOR MATCHES "x64")
        set(ARCH "x64")
    elseif (SYSTEM_PROCESSOR MATCHES "aarch64" OR SYSTEM_PROCESSOR MATCHES "arm64")
        set(ARCH "ARM64")
    endif ()

    add_library(WinPixEventRuntime INTERFACE)
    target_link_libraries(WinPixEventRuntime INTERFACE ./bin/${ARCH}/WinPixEventRuntime.lib)
    target_include_directories(WinPixEventRuntime INTERFACE Include)
endif ()