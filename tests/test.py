import os
import subprocess
import math

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'


def run_program(program_name):
    with open(f"tests/{program_name}.log", "w") as log_file:
        subprocess.run(['python3', 'compiler.py', f'programs/{program_name}_test.s'], stdout=log_file, stderr=log_file)
        subprocess.run(['gcc', 'main.c', '-o', 'main'])
        subprocess.run(['./main', f'programs/{program_name}_test.bin', f'programs/{program_name}_state.txt'], stdout=log_file, stderr=log_file)


def test_init():
    program_name = "init"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0x0123456789abcdef
    expected_r1 = 0xa5a5a5a5a5a5a5a5
    expected_r2 = 0xaef45d745aff584f
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_add128():
    program_name = "add128"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
        r3 = int([line.strip() for line in lines if line.startswith('R3')][0].split(" = ")[1], 16)
        r4 = int([line.strip() for line in lines if line.startswith('R4')][0].split(" = ")[1], 16)
        r5 = int([line.strip() for line in lines if line.startswith('R5')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0x24152dfb45da45df
    expected_r1 = 0xa521147fde45f45a
    expected_r2 = 0x45dcea451f2d45a4
    expected_r3 = 0xf5554ed4f4522365
    expected_r4 = 0x69f2184065078b84
    expected_r5 = 0x9a766354d29817bf
    expected_res = (expected_r4 << 64) | expected_r5
    res = ((expected_r0 << 64) | expected_r1) + ((expected_r2 << 64) | expected_r3)
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and r3 == expected_r3 and r4 == expected_r4 and r5 == expected_r5 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_lshift64_128():
    program_name = "lshift64_128"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
        r3 = int([line.strip() for line in lines if line.startswith('R3')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0xf458f452145147de
    expected_r1 = 0xc
    expected_r2 = 0xf45
    expected_r3 = 0x8f452145147de000
    expected_res = (expected_r2 << 64) | expected_r3
    res = expected_r0 << expected_r1
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and r3 == expected_r3 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_lshift128():
    program_name = "lshift128"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
        r3 = int([line.strip() for line in lines if line.startswith('R3')][0].split(" = ")[1], 16)
        r4 = int([line.strip() for line in lines if line.startswith('R4')][0].split(" = ")[1], 16)
        r5 = int([line.strip() for line in lines if line.startswith('R5')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0x24152dfb45da45df
    expected_r1 = 0xa521147fde45f45a
    expected_r2 = 0xc
    expected_r3 = 0x241
    expected_r4 = 0x52dfb45da45dfa52
    expected_r5 = 0x1147fde45f45a000
    expected_res = (expected_r3 << 128) | (expected_r4 << 64) | expected_r5
    res = ((expected_r0 << 64) | expected_r1) << expected_r2
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and r3 == expected_r3 and r4 == expected_r4 and r5 == expected_r5 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_mul64():
    program_name = "mul64"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
        r3 = int([line.strip() for line in lines if line.startswith('R3')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0xfebc45fe4512695f
    expected_r1 = 0xf48ef54a
    expected_r2 = 0xf359b338
    expected_r3 = 0xfe48703f94dc6076
    expected_res = (expected_r2 << 64) | expected_r3
    res = expected_r0 * expected_r1
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and r3 == expected_r3 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_fac64_128():
    program_name = "fac64_128"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0x1e
    expected_r1 = 0xd13f6370f96
    expected_r2 = 0x865df5dd54000000
    expected_res = (expected_r1 << 64) | expected_r2
    res = math.factorial(expected_r0)
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def test_cmp():
    program_name = "cmp"
    run_program(program_name)
    with open(f"tests/{program_name}.log", 'r') as f:
        lines = f.readlines()
        r0 = int([line.strip() for line in lines if line.startswith('R0')][0].split(" = ")[1], 16)
        r1 = int([line.strip() for line in lines if line.startswith('R1')][0].split(" = ")[1], 16)
        r2 = int([line.strip() for line in lines if line.startswith('R2')][0].split(" = ")[1], 16)
    os.remove(f"tests/{program_name}.log")
    expected_r0 = 0x1
    expected_r1 = 0x2
    expected_r2 = 0xaf
    expected_res = 0xaf
    res = 0xfe if expected_r0 > expected_r1 else 0xaf
    if r0 == expected_r0 and r1 == expected_r1 and r2 == expected_r2 and res == expected_res:
        print(f"Program '{program_name}' -> {OKGREEN}PASSED{ENDC}")
        return 1
    else:
        print(f"Program '{program_name}' -> {FAIL}FAILED{ENDC}")
        return 0


def main():
    print("WELCOME TO THE TEST PROGRAM!")
    print("Testing all programs...")
    res = 0
    res += test_init()
    res += test_add128()
    res += test_lshift64_128()
    res += test_lshift128()
    res += test_mul64()
    res += test_fac64_128()
    res += test_cmp()
    if res == 7:
        print(f"{OKGREEN}ALL TESTS PASSED{ENDC}")
    else:
        print(f"{FAIL}ONE OR MORE TESTS FAILED{ENDC}")
    os.system("make clean")


if __name__ == "__main__":
    main()