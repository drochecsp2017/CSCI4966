# Part 1

## Step 1

```root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1# cmake -S /root/lab5/cmake/Tests/Tutorial/Step1/ -B ./build
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning (dev) in CMakeLists.txt:
  No cmake_minimum_required command is present.  A line of code such as

    cmake_minimum_required(VERSION 3.13)

  should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000".
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step1/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1# cd build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1/build# make
Scanning dependencies of target Tutorial
[ 50%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1/build# ./Tutorial
./Tutorial Version 1.0
Usage: ./Tutorial number
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1/build# ./Tutorial 4294967296
The square root of 4.29497e+09 is 65536
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step1/build# ./Tutorial 10
The square root of 10 is 3.16228```
