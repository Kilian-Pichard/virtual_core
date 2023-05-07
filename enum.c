//
// Created by Kilian Pichard on 27/04/2023.
//

enum Register
{
    R0 = 0x00,
    R1 = 0x01,
    R2 = 0x02,
    R3 = 0x03,
    R4 = 0x04,
    R5 = 0x05,
    R6 = 0x06,
    R7 = 0x07,
    R8 = 0x08,
    R9 = 0x09,
    R10 = 0x0a,
    R11 = 0x0b,
    R12 = 0x0c,
    R13 = 0x0d,
    R14 = 0x0e,
    R15 = 0x0f,
};

enum Opcode {
    AND = 0x00, // 0x00 -> Logical AND -> AND -> dest = ope1 and ope2
    ORR = 0x01, // 0x01 -> Logical OR -> ORR -> dest = ope1 or ope2
    EOR = 0x02, // 0x02 -> Logical XOR -> EOR -> dest = ope1 xor ope2
    ADD = 0x03, // 0x03 -> Addition -> ADD -> dest = ope1 + ope2
    ADC = 0x04, // 0x04 -> Addition with carry -> ADC -> dest = ope1 + ope2 + carry
    CMP = 0x05, // 0x05 -> Comparison -> CMP -> See section on CMP (2.5.5)
    SUB = 0x06, // 0x06 -> Subtraction -> SUB -> dest = ope1 - ope2
    SBC = 0x07, // 0x07 -> Subtraction with carry -> SBC -> dest = ope1 - ope2 + carry - 1
    MOV = 0x08, // 0x08 -> Move data -> MOV -> dest = ope2
    LSH = 0x09, // 0x09 -> Logical left shift -> LSH -> dest = ope1 << ope2
    RSH = 0x0a, // 0x0a -> Logical right shift -> RSH -> dest = ope1 >> ope2
};

enum BranchConditionCode {
    B   = 0x8, // 0x8 -> Unconditional branch
    BEQ = 0x9, // 0x9 -> Branch if equal
    BNE = 0xa, // 0xa -> Branch if not equal
    BLE = 0xb, // 0xb -> Branch if lower or equal
    BGE = 0xc, // 0xc -> Branch if greater or equal
    BL  = 0xd, // 0xd -> Branch if lower
    BG  = 0xe, // 0xe -> Branch if greater
};
