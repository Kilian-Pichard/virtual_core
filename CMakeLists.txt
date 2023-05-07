cmake_minimum_required(VERSION 3.25)
project(virtual_core C)

set(CMAKE_C_STANDARD 11)

add_executable(virtual_core main.c functions.c enum.c)
