//
// Created by Kilian Pichard on 27/04/2023.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "enum.c"
#define BUFFER_SIZE 4

static const char *registers[] = {
        [R0] = "R0",
        [R1] = "R1",
        [R2] = "R2",
        [R3] = "R3",
        [R4] = "R4",
        [R5] = "R5",
        [R6] = "R6",
        [R7] = "R7",
        [R8] = "R8",
        [R9] = "R9",
        [R10] = "R10",
        [R11] = "R11",
        [R12] = "R12",
        [R13] = "R13",
        [R14] = "R14",
        [R15] = "R15",
};

static int BCC_B = 1;
static int BCC_BEQ = 0;
static int BCC_BNE = 0;
static int BCC_BLE = 0;
static int BCC_BGE = 0;
static int BCC_BL = 0;
static int BCC_BG = 0;
static uint8_t BCC;
static uint8_t OFFSET;
static uint8_t IV_FLAG;
static uint8_t OPCODE;
static uint8_t FIRSTOPE;
static uint8_t SECONDOPE;
static uint8_t DEST;
static uint8_t IV;
static uint64_t OPE1;
static uint64_t OPE2;

int program_counter = 0;
uint32_t carry = 0;
uint64_t regs[16] = {0};

uint32_t fetch(FILE *file, int is_verbose);
void decode(uint32_t instruction, int is_verbose);
void execute(int is_verbose);

void print_registers() {
    //printf("Printing registers...\n");
    for(int i=0 ; i<16 ; i++) {
        printf("%s = 0x%llx\n", registers[i], regs[i]);
    }
}

void initRegisters(FILE*fptr) {
    printf("Start initializing registers...\n");
    char line[100];
    int index = 0;
    while(fgets(line, sizeof(line), fptr) != NULL) {
        //printf("Line %d: %s\n", index, line);
        char *lineArray[2];
        int i = 0;
        char *test = strtok(line, "=");
        while (test != NULL) {
            lineArray[i++] = test;
            test = strtok(NULL, "=");
        }

        char *endptr;
        unsigned long int result;
        for(enum Register r=R0 ; r!=R15 ; r=(enum Register)(r+1)) {
            if(strcmp(lineArray[0], registers[r]) == 0){
                regs[r] = strtoul(lineArray[1], &endptr, 16);
            }
        }
        index++;
    }
    printf("Registers initialized!\n");

    //Print registers
    //print_registers();
}

void print_byte_as_bits(uint8_t val) {
    for (int i = 7; 0 <= i; i--)
        printf("%c", (val & (1 << i)) ? '1' : '0');
    putchar(' ');
}

// Print an instruction as bits
void print_instruction_as_bits(uint32_t instruction) {
    for (int i = 31; 0 <= i; i--) {
        printf("%c", (instruction & (1 << i)) ? '1' : '0');
        if (i % 8 == 0) {
            putchar(' ');
        }
    }
    putchar('\n');
}

void print_branch_flags() {
    printf("B = %d\n", BCC_B);
    printf("BEQ = %d\n", BCC_BEQ);
    printf("BNE = %d\n", BCC_BNE);
    printf("BLE = %d\n", BCC_BLE);
    printf("BGE = %d\n", BCC_BGE);
    printf("BL = %d\n", BCC_BL);
    printf("BG = %d\n", BCC_BG);
}


//uint8_t getBCC(uint8_t *buffer);
uint8_t getBCC(const uint8_t *buffer);
uint8_t getOFFSET(const uint8_t *buffer);
uint8_t getIVFLAG(const uint8_t *buffer);
uint8_t getOPCODE(const uint8_t *buffer);
uint8_t getFIRSTOPE(const uint8_t *buffer);
uint8_t getSECONDOPE(const uint8_t *buffer);
uint8_t getDEST(const uint8_t *buffer);
uint8_t getIV(const uint8_t *buffer);

/*
uint8_t getBCC(const uint8_t *buffer) {
    uint8_t BCC = buffer[0] >> 4;
    //print_byte_as_bits(BCC);
    //printf("BCC = 0x%02x\n", BCC);
    return BCC;
}

uint8_t getOFFSET(const uint8_t *buffer) {
    uint8_t OFFSET = (buffer[0] & 0x0F) >> 3;
    //print_byte_as_bits(OFFSET);
    //printf("OFFSET = 0x%02x\n", OFFSET);
    return OFFSET;
}

uint8_t getIVFLAG(const uint8_t *buffer) {
    uint8_t IV_FLAG = buffer[0] & 0x07;
    //print_byte_as_bits(IV_FLAG);
    //printf("IV_FLAG = 0x%02x\n", IV_FLAG);
    return IV_FLAG;
}

uint8_t getOPCODE(const uint8_t *buffer) {
    uint8_t OPCODE = buffer[1] >> 4;
    //print_byte_as_bits(OPCODE);
    //printf("OPCODE = 0x%02x\n", OPCODE);
    return OPCODE;
}

uint8_t getFIRSTOPE(const uint8_t *buffer) {
    uint8_t FIRSTOPE = buffer[1] & 0x0F;
    //print_byte_as_bits(FIRSTOPE);
    //printf("FIRSTOPE = 0x%02x\n", FIRSTOPE);
    return regs[FIRSTOPE];
}

uint8_t getSECONDOPE(const uint8_t *buffer) {
    uint8_t SECONDOPE = buffer[2] >> 4;
    if(getIVFLAG(buffer) == 0x01) {
        SECONDOPE = getIV(buffer);
    } else {
        SECONDOPE = regs[SECONDOPE];
    }
    //print_byte_as_bits(SECONDOPE);
    //printf("SECONDOPE = 0x%02x\n", SECONDOPE);
    return SECONDOPE;
}

uint8_t getDEST(const uint8_t *buffer) {
    uint8_t DEST = buffer[2] & 0x0F;
    //print_byte_as_bits(DEST);
    //printf("DEST = 0x%02x\n", DEST);
    return DEST;
}

uint8_t getIV(const uint8_t *buffer) {
    uint8_t IV = buffer[3];
    //print_byte_as_bits(IV);
    //printf("IV = 0x%02x\n", IV);
    return IV;
}*/

int compute_next_PC(uint32_t instruction) {
    int offset = (int)(int32_t)(instruction & 0x7FFFFFF);
    int sign = ((instruction & 0x8000000) == 0) ? 1 : -1;
    return program_counter + (sign * offset);
}

int BCC_is_verified(uint8_t BCC_value) {
    int is_verified = 0;
    switch (BCC_value) {
        case BEQ:
            if(BCC_BEQ == 1) is_verified = 1;
            break;
        case BNE:
            if(BCC_BNE == 1) is_verified = 1;
            break;
        case BLE:
            if(BCC_BLE == 1) is_verified = 1;
            break;
        case BGE:
            if(BCC_BGE == 1) is_verified = 1;
            break;
        case BL:
            if(BCC_BL == 1) is_verified = 1;
            break;
        case BG:
            if(BCC_BG == 1) is_verified = 1;
            break;
        default:
            is_verified = 1;
            break;
    }
    return is_verified;
}

uint32_t swap_endian(uint32_t value) {
    return ((value >> 24) & 0xff) |
           ((value >> 8) & 0xff00) |
           ((value << 8) & 0xff0000) |
           ((value << 24) & 0xff000000);
}

void loop_program(FILE *file, int is_verbose) {
    uint32_t instruction;

    fseek(file, 0, SEEK_END);
    int file_size = (int)ftell(file);
    fseek(file, 0, SEEK_SET);
    int number_instructions = file_size / 4;
    printf("Number of instructions: %d\n", number_instructions);

    while(program_counter >= 0 && program_counter < number_instructions) {
        instruction = fetch(file, is_verbose);
        decode(instruction, is_verbose);
        execute(is_verbose);
    }

    if (!is_verbose) print_registers();

    if (program_counter < 0 ) {
        printf("\nError: program counter out of bounds.\n");
        exit(EXIT_FAILURE);
    } else {
        printf("\nProgram terminated successfully.\n");
        exit(EXIT_SUCCESS);
    }
}

uint32_t fetch(FILE *file, int is_verbose) {
    int next_PC;
    uint32_t instruction;

    // Set the file position indicator to the start of the third instruction
    int instruction_size = sizeof(instruction);
    int instruction_index = program_counter; // index of the third instruction is 2 (0-based index)
    fseek(file, instruction_index * instruction_size, SEEK_SET);

    // Read the third instruction from the file
    fread(&instruction, instruction_size, 1, file);

    //fread(&instruction, sizeof(instruction), 1, file);
    instruction = swap_endian(instruction);

    uint8_t BCC_value = instruction >> 28;
    uint8_t OFFSET_value = (instruction >> 27) & 0x01;
    int is_branch = (BCC_value == 0 ? 0 : 1);
    if (is_branch && BCC_is_verified(BCC_value)) {
        next_PC = compute_next_PC(instruction);
    } else {
        next_PC = program_counter + 1;
    }

    if(is_verbose) {
        printf("Start fetching...\n");
        printf("Instruction %d (hex): 0x%08x\n", program_counter, instruction);
        printf("Instruction %d (bin): ", program_counter);
        print_instruction_as_bits(instruction);
        printf("BCC = 0x%01x\n", BCC_value);
        printf("OFFSET = %d\n", OFFSET_value);
        printf("PC = %d\n", program_counter);
        printf("End fetching...\n");
    }

    program_counter = next_PC;

    return instruction;
}

// Read the instruction to be executed from the code and compute the new value of the PC.
/*void fetch(FILE *file, int is_verbose) {
    printf("Start fetching...\n");
    int next_PC;
    uint32_t instruction;

    printf("PROGRAM COUNTER = %d\n", program_counter);
    printf("NUMBER INSTRUCTIONS = %d\n", number_instructions);
    if (program_counter < 0 ) {
        printf("\nError: program counter out of bounds.\n");
        printf("Following instruction cannot be fetched.\n");
        printf("Please find below the current state of the registers:\n");
        print_registers();
        exit(EXIT_FAILURE);
    }


    fread(&instruction, sizeof(instruction), program_counter, file);
    instruction = swap_endian(instruction);
    uint8_t BCC_value = instruction >> 28;
    uint8_t OFFSET_value = (instruction >> 27) & 0x01;
    int is_branch = (BCC_value == 0 ? 0 : 1);
    if (is_branch && BCC_is_verified(BCC_value)) {
        next_PC = compute_next_PC(instruction);
    } else {
        next_PC = program_counter + 1;
    }

    if(is_verbose) {
        printf("Instruction %d (hex): 0x%08x\n", program_counter, instruction);
        printf("Instruction %d (bin): ", program_counter);
        print_instruction_as_bits(instruction);
        printf("BCC = 0x%01x\n", BCC_value);
        printf("OFFSET = %d\n", OFFSET_value);
        printf("PC = %d\n", program_counter);
        putchar ('\n');
    }

    decode(instruction);
    execute(is_branch);

    // Update the PC and fetch the next instruction.
    program_counter = next_PC;
    fetch(file, is_verbose);

}*/

// Decode the instruction and read the operands from the registers.
void decode(uint32_t instruction, int is_verbose) {
    BCC = instruction >> 28;
    OFFSET = (instruction >> 27) & 0x01;
    IV_FLAG = (instruction >> 24) & 0x01;
    OPCODE = (instruction >> 20) & 0x0F;
    FIRSTOPE = (instruction >> 16) & 0x0F;
    SECONDOPE = (instruction >> 12) & 0x0F;
    DEST = (instruction >> 8) & 0x0F;
    IV = instruction & 0xFF;
    OPE1 = regs[FIRSTOPE];
    if(IV_FLAG == 0x01) {
        OPE2 = IV;
    } else {
        OPE2 = regs[SECONDOPE];
    }

    if (is_verbose) {
        printf("Start decoding...\n");
        printf("IV_FLAG = %d\n", IV_FLAG);
        printf("OPCODE = 0x%x\n", OPCODE);
        printf("FIRSTOPE = 0x%x\n", FIRSTOPE);
        printf("SECONDOPE = 0x%x\n", SECONDOPE);
        printf("DEST = 0x%x\n", DEST);
        printf("IV = 0x%x\n", IV);
        printf("OPE1 = 0x%llx\n", OPE1);
        printf("OPE2 = 0x%llx\n", OPE2);
        printf("End decoding...\n");
    }
}

void execute(int is_verbose) {
    uint64_t result;
    int is_branch = (BCC == 0 ? 0 : 1);
    if (!is_branch) {
        switch (OPCODE) {
            case AND:
                regs[DEST] = OPE1 & OPE2;
                break;
            case ORR:
                regs[DEST] = OPE1 | OPE2;
                break;
            case EOR:
                regs[DEST] = OPE1 ^ OPE2;
                break;
            case ADD:
                result = OPE1 + OPE2;
                carry = (result < OPE1 || result < OPE2) ? 1 : 0;
                regs[DEST] = result & 0xFFFFFFFFFFFFFFFF;
                break;
            case ADC:
                result = OPE1 + OPE2 + carry;
                carry = (result < OPE1 || result < OPE2) ? 1 : 0;
                regs[DEST] = result & 0xFFFFFFFFFFFFFFFF;
                break;
            case CMP:
                BCC_BEQ = (OPE1 == OPE2) ? 1 : 0;
                BCC_BNE = (OPE1 != OPE2) ? 1 : 0;
                BCC_BLE = (OPE1 <= OPE2) ? 1 : 0;
                BCC_BGE = (OPE1 >= OPE2) ? 1 : 0;
                BCC_BL = (OPE1 < OPE2) ? 1 : 0;
                BCC_BG = (OPE1 > OPE2) ? 1 : 0;
                break;
            case SUB:
                regs[DEST] = OPE1 - OPE2;
                break;
            case SBC:
                regs[DEST] = OPE1 - OPE2 + carry - 1;
                break;
            case MOV:
                regs[DEST] = OPE2;
                break;
            case LSH:
                regs[DEST] = OPE1 << OPE2;
                break;
            case RSH:
                regs[DEST] = OPE1 >> OPE2;
                break;
            default:
                break;
        }
    }

    if (is_verbose) {
        printf("Start executing...\n");
        printf("Carry = %d\n", carry);
        print_registers();
        print_branch_flags();
        printf("End executing...\n");
        putchar('\n');
    }
}