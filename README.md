# Practical Work: Virtual core implementation

This project involves implementing a 64-bit executable file on a Debian 11 distribution, with a core consisting of up to sixteen internal registers. The binary takes two mandatory and one optional argument, including the code to be executed, the initial state of the registers, and a flag for verbose mode. The instruction set includes operations such as logical AND/OR/XOR, addition/subtraction with carry, data movement, and logical shifts, with branching options based on comparison results. The project requires implementing functions for fetching, decoding, and executing instructions, along with testing and optional verbose mode.

## Installation

1. Clone this repository to your local machine. 
2. Navigate to the root directory of the project in your terminal. 
3. Run `make` or `make run` command to build and run the program. 
4. Run `make doc` command to generate documentation using Doxygen. 
5. Run `make clean` command to clean up generated binaries and documentation.

## Usage

1. Run `make` or `make run` command to build and run the program. This will prompt you to select a program to run from a list of available programs. You can also choose to run the program in verbose mode. 
2. Run `make doc` command to generate documentation using Doxygen. This will generate documentation in the ./doc folder. 
3. Run `make clean` command to clean up generated binaries and documentation.

If you want to compile and/or run a file by your own, you can use the following commands:
 - Compile: `python3 compiler.py <assembly_file.s>`
 - Run: `gcc main.c -o main && ./main <binary_file.bin> <registers_file.txt> (VERBOSE)`

## Documentation

Please refer to the **documentation** folder for more information about the project. You must run `make doc` command to generate the documentation of the virtual core first.

 - The documentation of the virtual core is available in the **documentation/html** and **documentation/latex** folders.
 - The documentation of the compiler is available in the **documentation/DocCompiler.md** file.

## Authors

 - Kilian Pichard
 - Loïc Gavens

## License

This project is licensed under the MIT License - see the **LICENSE** file for details.