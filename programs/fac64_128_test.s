MOV r1, r0
MOV r6, 1
MOV r7, r1
ADD r7, r7, 1
MOV r1, 0
MOV r2, 1

CMP r6, r7
BEQ 14

MOV r5, r6
CMP r5, 0
BEQ 5
ADD r4, r4, r2
ADC r3, r3, r1
SUB r5, r5, 1
B -5

MOV r1, r3
MOV r2, r4
MOV r3, 0
MOV r4, 0
ADD r6, r6, 1

B -14
MOV r6, 0
MOV r7, 0