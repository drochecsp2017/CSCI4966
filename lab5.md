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

## Makefile:
```
# makefile test
all: static_block dynamic_block

# programs themselves
static_block: program.o libblock.a
        cc program.o libblock.a -o static_block

dynamic_block: program.o libblock.so
        cc program.o libblock.so -o dynamic_block -Wl,-rpath='$ORIGIN'

# libraries
libblock.a: block.o
        ar qc libblock.a block.o

libblock.so: block.o
        cc block.o -shared -o libblock.so

#shared files
program.o: program.c
        cc -c program.c -o program.o

block.o: source/block.c headers/block.h
        cc -fPIC -c source/block.c -o block.o
```

## CMakefile:
```
cmake_minimum_required(VERSION 3.3)
project(Lib_Tutorial)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# create static library
add_library(libblock STATIC
        source/block.c)

# create shared library
add_library(dylibblock SHARED
        source/block.c)

# add the executable
add_executable(static_block program.c)
target_link_libraries(static_block libblock)
add_executable(dynamic_block program.c)
target_link_libraries(dynamic_block dylibblock)
```

## CMake makefile:
```
# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f
# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/lab5/part2/Lab-Example

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/lab5/part2/Lab-Example/build

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
        @$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
        /usr/local/bin/cmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
        @$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
        /usr/local/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
        $(CMAKE_COMMAND) -E cmake_progress_start /root/lab5/part2/Lab-Example/build/CMakeFiles /root/lab5/part2/Lab-Example/build/CMakeFiles/progress.marks
        $(MAKE) -f CMakeFiles/Makefile2 all
        $(CMAKE_COMMAND) -E cmake_progress_start /root/lab5/part2/Lab-Example/build/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
        $(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
        $(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
        $(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
        $(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named libblock

# Build rule for target.
libblock: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 libblock
.PHONY : libblock

# fast build rule for target.
libblock/fast:
        $(MAKE) -f CMakeFiles/libblock.dir/build.make CMakeFiles/libblock.dir/build
.PHONY : libblock/fast

#=============================================================================
# Target rules for targets named static_block

# Build rule for target.
static_block: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 static_block
.PHONY : static_block

# fast build rule for target.
static_block/fast:
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/build
.PHONY : static_block/fast

#=============================================================================
# Target rules for targets named dylibblock

# Build rule for target.
dylibblock: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 dylibblock
.PHONY : dylibblock

# fast build rule for target.
dylibblock/fast:
        $(MAKE) -f CMakeFiles/dylibblock.dir/build.make CMakeFiles/dylibblock.dir/build
.PHONY : dylibblock/fast

#=============================================================================
# Target rules for targets named dynamic_block

# Build rule for target.
dynamic_block: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 dynamic_block
.PHONY : dynamic_block

# fast build rule for target.
dynamic_block/fast:
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/build
.PHONY : dynamic_block/fast

program.o: program.c.o

.PHONY : program.o

# target to build an object file
program.c.o:
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.o
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.o
.PHONY : program.c.o
program.i: program.c.i

.PHONY : program.i

# target to preprocess a source file
program.c.i:
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.i
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.i
.PHONY : program.c.i

program.s: program.c.s

.PHONY : program.s

# target to generate assembly for a file
program.c.s:
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.s
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.s
.PHONY : program.c.s

source/block.o: source/block.c.o

.PHONY : source/block.o

# target to build an object file
source/block.c.o:
        $(MAKE) -f CMakeFiles/libblock.dir/build.make CMakeFiles/libblock.dir/source/block.c.o
        $(MAKE) -f CMakeFiles/dylibblock.dir/build.make CMakeFiles/dylibblock.dir/source/block.c.o
.PHONY : source/block.c.o

source/block.i: source/block.c.i

.PHONY : source/block.i

# target to preprocess a source file
source/block.c.i:
        $(MAKE) -f CMakeFiles/libblock.dir/build.make CMakeFiles/libblock.dir/source/block.c.i
        $(MAKE) -f CMakeFiles/dylibblock.dir/build.make CMakeFiles/dylibblock.dir/source/block.c.i
.PHONY : source/block.c.i

source/block.s: source/block.c.s

.PHONY : source/block.s

# target to generate assembly for a file
source/block.c.s:
        $(MAKE) -f CMakeFiles/libblock.dir/build.make CMakeFiles/libblock.dir/source/block.c.s
        $(MAKE) -f CMakeFiles/dylibblock.dir/build.make CMakeFiles/dylibblock.dir/source/block.c.s
.PHONY : source/block.c.s

# Help Target
help:
        @echo "The following are some of the valid targets for this Makefile:"
        @echo "... all (the default if no target is provided)"
        @echo "... clean"
        @echo "... depend"
        @echo "... rebuild_cache"
        @echo "... edit_cache"
        @echo "... libblock"
        @echo "... static_block"
        @echo "... dylibblock"
        @echo "... dynamic_block"
        @echo "... program.o"
        @echo "... program.i"
        @echo "... program.s"
        @echo "... source/block.o"
        @echo "... source/block.i"
        @echo "... source/block.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
        $(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system
```


## Relative sizes (from `ls -la`):
```
-rwxrwxrwx 1 root root  8600 Feb 12 22:36 dynamic_block
-rwxrwxrwx 1 root root  8784 Feb 12 22:30 static_block
```

## Output:
```
root@DESKTOP-1O100B3:~/lab5/part2/Lab-Example/build# ./static_block
d y n a m i c   o r   s t a t i c
y n a m i c   o r   s t a t i c d
n a m i c   o r   s t a t i c d y
a m i c   o r   s t a t i c d y n
m i c   o r   s t a t i c d y n a
i c   o r   s t a t i c d y n a m
c   o r   s t a t i c d y n a m i
  o r   s t a t i c d y n a m i c
o r   s t a t i c d y n a m i c
r   s t a t i c d y n a m i c   o
  s t a t i c d y n a m i c   o r
s t a t i c d y n a m i c   o r
t a t i c d y n a m i c   o r   s
a t i c d y n a m i c   o r   s t
t i c d y n a m i c   o r   s t a
i c d y n a m i c   o r   s t a t
c d y n a m i c   o r   s t a t i
root@DESKTOP-1O100B3:~/lab5/part2/Lab-Example/build# ./dynamic_block
d y n a m i c   o r   s t a t i c
y n a m i c   o r   s t a t i c d
n a m i c   o r   s t a t i c d y
a m i c   o r   s t a t i c d y n
m i c   o r   s t a t i c d y n a
i c   o r   s t a t i c d y n a m
c   o r   s t a t i c d y n a m i
  o r   s t a t i c d y n a m i c
o r   s t a t i c d y n a m i c
r   s t a t i c d y n a m i c   o
  s t a t i c d y n a m i c   o r
s t a t i c d y n a m i c   o r
t a t i c d y n a m i c   o r   s
a t i c d y n a m i c   o r   s t
t i c d y n a m i c   o r   s t a
i c d y n a m i c   o r   s t a t
c d y n a m i c   o r   s t a t i
```
