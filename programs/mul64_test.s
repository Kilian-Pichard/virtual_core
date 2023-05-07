MOV r4, 32
MOV r5, 32

MOV r2, r0
RSH r2, r2, 32
LSH r0, r0, 32
RSH r0, r0, 32
MOV r3, r1
RSH r3, r3, 32
LSH r1, r1, 32
RSH r1, r1, 32

MOV r10, r0
MOV r11, r1
MOV r12, r2
MOV r13, r3
CMP r11, 0
BEQ 9
AND r15, r11, 1
CMP r15, 1
BNE 2
ADD r4, r4, r10
LSH r10, r10, 1
RSH r11, r11, 1
SUB r4, r4, 1
B -9

MOV r10, r0
MOV r11, r1
MOV r12, r2
MOV r13, r3
CMP r11, 0
BEQ 9
AND r15, r11, 1
CMP r15, 1
BNE 2
ADD r5, r5, r12
LSH r12, r12, 1
RSH r11, r11, 1
SUB r5, r5, 1
B -9

MOV r10, r0
MOV r11, r1
MOV r12, r2
MOV r13, r3
CMP r13, 0
BEQ 9
AND r15, r13, 1
CMP r15, 1
BNE 2
ADD r6, r6, r12
LSH r12, r12, 1
RSH r13, r13, 1
SUB r6, r6, 1
B -9

MOV r10, r0
MOV r11, r1
MOV r12, r2
MOV r13, r3
CMP r13, 0
BEQ 9
AND r15, r13, 1
CMP r15, 1
BNE 2
ADD r7, r7, r12
LSH r12, r12, 1
RSH r13, r13, 1
SUB r7, r7, 1
B -9

MOV r10, r4
LSH r11, r5, 32
LSH r12, r6, 32
MOV r13, 0
ADD r9, r10, r11
ADD r9, r9, r12
ADD r9, r9, r13

MOV r10, 0
RSH r11, r5, 32
RSH r12, r6, 32
RSH r13, r7
ADD r8, r10, r11
ADD r8, r8, r12
ADD r8, r8, r13

MOV r2, r8
MOV r3, r9
MOV r4, 0
MOV r5, 0
MOV r6, 0
MOV r7, 0
MOV r8, 0
MOV r9, 0
MOV r10, 0
MOV r11, 0
MOV r12, 0
MOV r13, 0
MOV r14, 0
MOV r15, 0