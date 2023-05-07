MOV r0, 1
MOV r3, 0
MOV r4, 1
CMP r3, 6
ADD r4, r4, 34
ADD r3, r3, 1
LSH r0, r0, 8
ORR r0, r0, r4
BL -5

MOV r1, 165
MOV r3, 0
CMP r3, 6
ADD r3, r3, 1
LSH r1, r1, 8
ORR r1, r1, 165
BL -4

MOV r2, 174
LSH r2, r2, 8
ORR r2, r2, 244
LSH r2, r2, 8
ORR r2, r2, 93
LSH r2, r2, 8
ORR r2, r2, 116
LSH r2, r2, 8
ORR r2, r2, 90
LSH r2, r2, 8
ORR r2, r2, 255
LSH r2, r2, 8
ORR r2, r2, 88
LSH r2, r2, 8
ORR r2, r2, 79