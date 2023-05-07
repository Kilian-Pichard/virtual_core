#include <stdio.h>
#include <stdlib.h>
#include "functions.c"

int main(int argc, char **argv) {
    // Usage example : BIN_NAME <CODE> <STATE> (VERBOSE)
    // Example: ./main compiled.bin reginit.txt

    // Check if the user has entered the correct number of arguments
    if(argc < 3) {
        printf("Usage : %s <CODE> <STATE> (VERBOSE)\n\n", argv[0]);
        return 1;
    }

    // Check if program is in verbose mode
    int is_verbose = 0;
    if(argc == 4 && (strcmp(argv[3], "VERBOSE") == 0)) {
        printf("Program is running in verbose mode.\n");
        is_verbose = 1;
    }

    // Initialize registers
    FILE *fptr = fopen(argv[2], "r");
    if (fptr == NULL) {
        printf("Error while opening file!\n");
        exit(1);
    }
    initRegisters(fptr);
    fclose(fptr);

    // Initialize memory
    FILE *binary_file = fopen(argv[1], "rb");
    if (binary_file == NULL) {
        printf("Error while opening file!\n");
        exit(1);
    }

    // Fetch instructions and close file
    loop_program(binary_file, is_verbose);

    print_registers();

    fclose(binary_file);
}
