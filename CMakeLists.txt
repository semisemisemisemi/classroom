cmake_minimum_required(VERSION 3.10)

project(Calculator)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

add_executable(calculator src/main.cpp src/calculator.cpp)

enable_testing()
add_executable(test_calculator tests/test_calculator.cpp src/calculator.cpp)
add_test(NAME calculator_test COMMAND test_calculator)
