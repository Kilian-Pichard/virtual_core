# In order to see the compiled.bin file on the terminal, use this command:
# - in binary format: $ xxd -b compiled.bin
# - in hex format: $ hexdump -C compiled.bin
# If offset of BCC is positive, bit 27 is equal to 0, otherwise it's equal to 1

import sys
import os

EXIT_ERROR = -1

# Registers values
R0 = b'\x00'    # 0x00
R1 = b'\x01'    # 0x01
R2 = b'\x02'    # 0x02
R3 = b'\x03'    # 0x03
R4 = b'\x04'    # 0x04
R5 = b'\x05'    # 0x05
R6 = b'\x06'    # 0x06
R7 = b'\x07'    # 0x07
R8 = b'\x08'    # 0x08
R9 = b'\x09'    # 0x09
R10 = b'\x0a'   # 0x0a
R11 = b'\x0b'   # 0x0b
R12 = b'\x0c'   # 0x0c
R13 = b'\x0d'   # 0x0d
R14 = b'\x0e'   # 0x0e
R15 = b'\x0f'   # 0x0f

# BCC values
B = b'\x08'         # 0x08
BEQ = b'\x09'       # 0x09
BNE = b'\x0a'       # 0x0a
BLE = b'\x0b'       # 0x0b
BGE = b'\x0c'       # 0x0c
BL = b'\x0d'        # 0x0d
BG = b'\x0e'        # 0x0e
BCC_NULL = b'\x00'  # 0x00

# Opcodes values
AND = b'\x00'           # 0x00
ORR = b'\x10'           # 0x10
EOR = b'\x20'           # 0x20
ADD = b'\x30'           # 0x30
ADC = b'\x40'           # 0x40
CMP = b'\x50'           # 0x50
SUB = b'\x60'           # 0x60
SBC = b'\x70'           # 0x70
MOV = b'\x80'           # 0x80
LSH = b'\x90'           # 0x90
RSH = b'\xa0'           # 0xa0
OPCODE_NULL = b'\x00'   # 0xf0


# Proceed a left shift of shift bits on input
def left_shift(input, shift):
    return ((int.from_bytes(input, byteorder="big")) << shift).to_bytes(1, byteorder='big')


# Proceed a bitwise OR between input1 and input2
def bitwise_or(input1, input2):
    return (int.from_bytes(input1, byteorder="big") | int.from_bytes(input2, byteorder="big")).to_bytes(1, byteorder="big")


# Get the register value
def get_register_value(register_string):
    if register_string == "r0":
        return R0
    elif register_string == "r1":
        return R1
    elif register_string == "r2":
        return R2
    elif register_string == "r3":
        return R3
    elif register_string == "r4":
        return R4
    elif register_string == "r5":
        return R5
    elif register_string == "r6":
        return R6
    elif register_string == "r7":
        return R7
    elif register_string == "r8":
        return R8
    elif register_string == "r9":
        return R9
    elif register_string == "r10":
        return R10
    elif register_string == "r11":
        return R11
    elif register_string == "r12":
        return R12
    elif register_string == "r13":
        return R13
    elif register_string == "r14":
        return R14
    elif register_string == "r15":
        return R15


# Main function: encode an instruction
def encode_instruction(instruction, instruction_args):
    BCC = BCC_NULL              # 4 bits
    OFFSET_IV_FLAG = b'\x00'    # 4 bits (3 bits offset + 1 bit IV flag)
    OPCODE = OPCODE_NULL        # 4 bits
    FIRST_OPERAND = b'\x00'     # 4 bits
    SECOND_OPERAND = b'\x00'    # 4 bits
    DEST = b'\x00'              # 4 bits
    IV = b'\x00'                # 8 bits

    if instruction.startswith("B"):  # Check if instruction is a BCC
        if instruction == "B":
            BCC = B
        elif instruction == "BEQ":
            BCC = BEQ
        elif instruction == "BNE":
            BCC = BNE
        elif instruction == "BLE":
            BCC = BLE
        elif instruction == "BGE":
            BCC = BGE
        elif instruction == "BL":
            BCC = BL
        elif instruction == "BG":
            BCC = BG
        if -255 <= int(instruction_args[0]) <= 255:  # Check if offset is a digit on 2 bytes, positive or negative
            if int(instruction_args[0]) < 0:
                IV = abs(int(instruction_args[0])).to_bytes(1, byteorder="big", signed=False)
                OFFSET_IV_FLAG = b'\x08'
            else:
                IV = int(instruction_args[0]).to_bytes(1, byteorder="big", signed=False)
        else:
            print("Error! Please use digit on 2 bytes (from -255 to 255).")
            exit(EXIT_ERROR)
    else:  # If instruction is not a BCC
        registers = list(filter(lambda x:x.startswith("r"), instruction_args))  # Get all registers of the instruction
        if len(registers) > 1:  # If there is at least 2 registers
            FIRST_OPERAND = get_register_value(registers[1])
        if len(registers) > 2:  # If there is at least 3 registers
            SECOND_OPERAND = left_shift(get_register_value(registers[2]), 4)
        if instruction == "AND":
            OPCODE = AND
            DEST = get_register_value(registers[0])
        elif instruction == "ORR":
            OPCODE = ORR
            DEST = get_register_value(registers[0])
        elif instruction == "EOR":
            OPCODE = EOR
            DEST = get_register_value(registers[0])
        elif instruction == "ADD":
            OPCODE = ADD
            DEST = get_register_value(registers[0])
        elif instruction == "ADC":
            OPCODE = ADC
            DEST = get_register_value(registers[0])
        elif instruction == "CMP":
            OPCODE = CMP
            if len(registers) > 0:  # If there is at least 1 register
                FIRST_OPERAND = get_register_value(registers[0])
            if len(registers) > 1:  # If there is at least 2 registers
                SECOND_OPERAND = left_shift(get_register_value(registers[1]), 4)
        elif instruction == "SUB":
            OPCODE = SUB
            DEST = get_register_value(registers[0])
        elif instruction == "SBC":
            OPCODE = SBC
            DEST = get_register_value(registers[0])
        elif instruction == "MOV":
            OPCODE = MOV
            DEST = get_register_value(registers[0])
            SECOND_OPERAND = left_shift(FIRST_OPERAND, 4)
            FIRST_OPERAND = b'\x00'
        elif instruction == "LSH":
            OPCODE = LSH
            DEST = get_register_value(registers[0])
        elif instruction == "RSH":
            OPCODE = RSH
            DEST = get_register_value(registers[0])
        immediate_value = list(filter(lambda x:x.isdigit(), instruction_args))  # Get immediate value of the instruction
        if immediate_value:  # Check if immediate value is not empty
            if int(immediate_value[0]) <= 255:
                IV = int(immediate_value[0]).to_bytes(1, byteorder="big", signed=False)
            else:
                print("Error! Please use digit on 2 bytes (max 255).")
                exit(EXIT_ERROR)
    if instruction_args[-1].isdigit() and not instruction.startswith("B"):  # IV is not empty
        IV_FLAG = b'\x01'
        OFFSET_IV_FLAG = bytes([OFFSET_IV_FLAG[0] + IV_FLAG[0]])
    return bitwise_or(left_shift(BCC, 4), OFFSET_IV_FLAG) + bitwise_or(OPCODE, FIRST_OPERAND) + bitwise_or(SECOND_OPERAND, DEST) + IV


def main():
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".s"):
        print("Error! Missing argument or invalid file extension.")
        print("Usage: python3 compiler.py <ASM.s>")
        exit(EXIT_ERROR)
    else:
        asm_file = sys.argv[1]

    if not os.path.isfile(asm_file):
        print("Error! File " + asm_file + " does not exist.")
        print("Usage: python3 compiler.py <ASM.s>")
        exit(EXIT_ERROR)

    with open(asm_file, "r") as f:
        lines = f.readlines()

    encoded = b''
    available_instructions = ["AND", "ORR", "EOR", "ADD", "ADC", "CMP", "SUB", "SBC", "MOV", "LSH", "RSH",
                              "B", "BEQ", "BNE", "BLE", "BGE", "BL", "BG"]
    for line in lines:  # Loop line by line in the read file in order to encode each instruction
        line_splited = line.strip().replace(",", "").split(" ")
        instruction = line_splited[0]
        instruction_args = line_splited[1:]
        if instruction in available_instructions:  # Check if instruction is available
            encoded = encoded + encode_instruction(instruction, instruction_args)

    # Write the encoded instructions in a binary file
    with open(os.path.splitext(asm_file)[0]+".bin", "wb+") as compiled_file:
        for byte in encoded:
            compiled_file.write(byte.to_bytes(1, byteorder='big'))
    print("File " + os.path.basename(asm_file) + " compiled with success!")


if __name__ == "__main__":
    main()
