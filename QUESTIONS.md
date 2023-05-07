# 4. Questions 

1. Which parts of a 64 bits processor are 64 bits wide ?
   In a 64-bit processor, several parts are 64 bits wide, including:
   - Registers: A 64-bit processor has 64-bit registers that can hold 64-bit data. These registers are used for various purposes, such as arithmetic operations, memory addressing, and control flow.
   - Address bus: The address bus is 64 bits wide, which means it can address up to 2^64 bytes of memory.
   - Data bus: The data bus is also 64 bits wide, which means it can transfer 64 bits of data between the processor and memory or other peripherals in a single cycle.
   - ALU (Arithmetic Logic Unit): The ALU is responsible for performing arithmetic and logical operations on the data stored in registers. In a 64-bit processor, the ALU is designed to work on 64-bit data.
   - Floating-point unit (FPU): The FPU is a specialized unit that performs floating-point arithmetic operations. In a 64-bit processor, the FPU is designed to work with 64-bit floating-point numbers.
   - Instruction pointer (IP): The IP is a register that holds the memory address of the next instruction to be executed. In a 64-bit processor, the IP is 64 bits wide, which means it can address up to 2^64 bytes of memory.
   Note that not all parts of a 64-bit processor are 64 bits wide. For example, the cache lines can vary in size and are typically smaller than 64 bits, and some instructions may operate on smaller data types, such as 8-bit or 16-bit.

2. Which instructions can potentially create a carry ?

3. What is the purpose of the add carry (ADC) instruction ?

4. What are the check to realize during a branch instruction ?

5. Is it possible to pipeline the virtual core ?
