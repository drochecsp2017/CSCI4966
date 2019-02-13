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
The square root of 10 is 3.16228

```````````

## Step 2


```
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step2# cmake -S /root/lab5/cmake/Tests/Tutorial/Step2/ -B build
-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step2/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step2# cd build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step2/build# make
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step2/build# ./Tutorial
./Tutorial Version 1.1
Usage: ./Tutorial number
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step2/build# ./Tutorial 44
Computing sqrt of 44 to be 22.5
Computing sqrt of 44 to be 12.2278
Computing sqrt of 44 to be 7.91307
Computing sqrt of 44 to be 6.73675
Computing sqrt of 44 to be 6.63404
Computing sqrt of 44 to be 6.63325
Computing sqrt of 44 to be 6.63325
Computing sqrt of 44 to be 6.63325
Computing sqrt of 44 to be 6.63325
Computing sqrt of 44 to be 6.63325
The square root of 44 is 6.63325
```

## Step 3
```
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step3# cmake -S ~/lab5/cmake/Tests/Tutorial/Step3/ -B ./build/
-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step3/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step3# cd build/
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step3/build# make
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step3/build# ./Tutorial
./Tutorial Version 1.1
Usage: ./Tutorial number
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step3/build# ./Tutorial 4
Computing sqrt of 4 to be 2.5
Computing sqrt of 4 to be 2.05
Computing sqrt of 4 to be 2.00061
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
Computing sqrt of 4 to be 2
The square root of 4 is 2
```

## Step 4
```
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4# cmake -S ~/lab5/cmake/Tests/Tutorial/Step4/ -B ./build/
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
-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step4/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4# cd build/
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# make
Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# make install
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
Install the project...
-- Install configuration: ""
-- Installing: /usr/local/bin/Tutorial
-- Installing: /usr/local/include/TutorialConfig.h
-- Installing: /usr/local/bin/libMathFunctions.a
-- Installing: /usr/local/include/MathFunctions.h
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# ./Tutorial 25
Computing sqrt of 25 to be 13
Computing sqrt of 25 to be 7.46154
Computing sqrt of 25 to be 5.40603
Computing sqrt of 25 to be 5.01525
Computing sqrt of 25 to be 5.00002
Computing sqrt of 25 to be 5
Computing sqrt of 25 to be 5
Computing sqrt of 25 to be 5
Computing sqrt of 25 to be 5
Computing sqrt of 25 to be 5
The square root of 25 is 5
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# cd ..
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4# nano CMakeLists.txt
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4# cmake -S ~/lab5/cmake/Tests/Tutorial/Step4/ -B ./build/
-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step4/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4# cd build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# make
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# ./Tutorial
./Tutorial Version 1.1
Usage: ./Tutorial number
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# ./Tutorial 20
Computing sqrt of 20 to be 10.5
Computing sqrt of 20 to be 6.20238
Computing sqrt of 20 to be 4.71347
Computing sqrt of 20 to be 4.47831
Computing sqrt of 20 to be 4.47214
Computing sqrt of 20 to be 4.47214
Computing sqrt of 20 to be 4.47214
Computing sqrt of 20 to be 4.47214
Computing sqrt of 20 to be 4.47214
Computing sqrt of 20 to be 4.47214
The square root of 20 is 4.47214
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step4/build# ctest -N
Test project /root/lab5/cmake/Tests/Tutorial/Step4/build
  Test #1: Runs
  Test #2: Usage
  Test #3: Comp25
  Test #4: Comp-25
  Test #5: Comp0.0001

Total Tests: 5
```

## Step 5 
```
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5/MathFunctions# cmake -S ~/lab5/cmake/Tests/Tutorial/Step5/MathFunctions/ -B ./build/
CMake Warning (dev) in CMakeLists.txt:
  No cmake_minimum_required command is present.  A line of code such as

    cmake_minimum_required(VERSION 3.13)

  should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000".
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step5/MathFunctions/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5/MathFunctions# cd build/ && make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object CMakeFiles/MathFunctions.dir/mysqrt.o
[100%] Linking CXX static library libMathFunctions.a
[100%] Built target MathFunctions
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5/MathFunctions/build# cd .. && cd ..
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5# cmake -S ~/lab5/cmake/Tests/Tutorial/Step5/ -B ./build/
-- Configuring done
-- Generating done
-- Build files have been written to: /root/lab5/cmake/Tests/Tutorial/Step5/build
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5# cd build/ && make
Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5/build# Tutorial
Tutorial Version 1.1
Usage: Tutorial number
root@DESKTOP-1O100B3:~/lab5/cmake/Tests/Tutorial/Step5/build# Tutorial 24
Computing sqrt of 24 to be 12.5
Computing sqrt of 24 to be 7.21
Computing sqrt of 24 to be 5.26936
Computing sqrt of 24 to be 4.912
Computing sqrt of 24 to be 4.899
Computing sqrt of 24 to be 4.89898
Computing sqrt of 24 to be 4.89898
Computing sqrt of 24 to be 4.89898
Computing sqrt of 24 to be 4.89898
Computing sqrt of 24 to be 4.89898
The square root of 24 is 4.89898
```

# Part 2

placeholder
