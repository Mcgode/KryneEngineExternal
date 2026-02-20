project(WinPixEventRuntime)

if (WIN32)
    if (CMAKE_SYSTEM_PROCESSOR MATCHES "AMD64")
        set(ARCH "x64")
    elseif (CMAKE_SYSTEM_PROCESSOR MATCHES "ARM64")
        set(ARCH "ARM64")
    endif ()

    add_library(WinPixEventRuntime SHARED IMPORTED GLOBAL)
    set_target_properties(WinPixEventRuntime PROPERTIES
            IMPORTED_IMPLIB     "${CMAKE_CURRENT_SOURCE_DIR}/bin/${ARCH}/WinPixEventRuntime.lib"
            IMPORTED_LOCATION   "${CMAKE_CURRENT_SOURCE_DIR}/bin/${ARCH}/WinPixEventRuntime.dll"
            INTERFACE_INCLUDE_DIRECTORIES   "${CMAKE_CURRENT_SOURCE_DIR}/Include"
    )
endif ()