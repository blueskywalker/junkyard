# example-poco-timer
Example timer with POCO C++ libraries installed with conan C and C++ package manager

mkdir build && cd build
conan install ..     // conan install .. --build missing
cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=release
cmake --build .
