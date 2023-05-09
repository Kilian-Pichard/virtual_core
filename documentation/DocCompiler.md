# Documentation of the compiler

## Table of contents
### 1. [Introduction](#introduction)
### 2. [Installation](#installation)
### 3. [Usage](#usage)
### 4. [Authors](#authors)
### 5. [License](#license)

## Introduction

This project involves implementing a compiler for a custom assembly language, which is then translated into a binary file that can be executed on a virtual core. The compiler is implemented in Python 3, and the virtual core is implemented in C. The compiler takes an assembly file as input and outputs a binary file that can be executed on the virtual core. The assembly language includes instructions such as logical AND/OR/XOR, addition/subtraction with carry, data movement, and logical shifts, with branching options based on comparison results. The virtual core consists of up to sixteen internal registers, and the binary takes two mandatory and one optional argument, including the code to be executed, the initial state of the registers, and a flag for verbose mode. The project requires implementing functions for fetching, decoding, and executing instructions, along with testing and optional verbose mode.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project in your terminal.
3. To use the compiler separately, run `python3 compiler.py <assembly_file.s>`. This will generate a binary file in the same directory as the assembly file.

## Usage

The compiler is divided into multiple functions:
 - `main()` is the main function of the compiler. It takes the assembly file as input and outputs a binary file. It calls the other functions of the compiler.
 - `encode_instruction(instrucrtion, instruction_args)` encodes an instruction and its arguments into a binary string. It returns the encoded instruction.
 - `get_register_value(register_string)` returns the value of a register. It returns the value as a binary string.
 - `bitwise_or(input1, input2)` performs a bitwise OR operation on two binary strings. It returns the result of the operation.
 - `left_shift(input, shift)` performs a left shift on a binary string. It returns the shifted string.

## Authors

 - Kilian Pichard

## License

This project is licensed under the MIT License - see the **[LICENSE](https://github.com/Kilian-Pichard/virtual_core/blob/main/LICENSE)** file for details.