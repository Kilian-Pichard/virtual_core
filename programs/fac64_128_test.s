MOV r5, 1
MOV r6, r0
ADD r6, r6, 1
MOV r0, 0
MOV r1, 1

CMP r5, r6
BEQ 14

MOV r4, r5
CMP r4, 0
BEQ 5
ADD r3, r3, r1
ADC r2, r2, r0
SUB r4, r4, 1
B -5

MOV r0, r2
MOV r1, r3
MOV r2, 0
MOV r3, 0
ADD r5, r5, 1

B -14
MOV r15, 0