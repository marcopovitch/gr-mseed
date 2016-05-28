INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MSEED mseed)

FIND_PATH(
    MSEED_INCLUDE_DIRS
    NAMES mseed/api.h
    HINTS $ENV{MSEED_DIR}/include
        ${PC_MSEED_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MSEED_LIBRARIES
    NAMES gnuradio-mseed
    HINTS $ENV{MSEED_DIR}/lib
        ${PC_MSEED_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MSEED DEFAULT_MSG MSEED_LIBRARIES MSEED_INCLUDE_DIRS)
MARK_AS_ADVANCED(MSEED_LIBRARIES MSEED_INCLUDE_DIRS)

