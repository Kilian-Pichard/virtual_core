MOV r2, 0
MOV r3, 0
MOV r4, 64
CMP r1, 0
BEQ 10
AND r5, r1, 1
CMP r5, 1
BNE 3
ADD r2, r2, r0
ADC r3, r3, 0
LSH r0, r0, 1
RSH r1, r1, 1
SUB r4, r4, 1
B -10
MOV r6, 0