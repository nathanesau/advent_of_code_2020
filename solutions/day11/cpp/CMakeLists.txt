cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 17)

project(day11)

add_executable(solution solution.cpp)

file(COPY ../assets DESTINATION ${CMAKE_BINARY_DIR})