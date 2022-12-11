def showCrt(crt_screen):
    for line in crt_screen:
        for char in line:
            print(char, end="")
        print()

def part1(data):
    instructions = [line.split(" ") for line in data.split("\n")]
    x = 1
    cycle = 0
    signal_strength = 0
    for instruction in instructions:
        if instruction[0] == "noop":
            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle <= 220: 
                signal_strength += cycle * x
        else:
            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle <= 220: 
                signal_strength += cycle * x
            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle <= 220: 
                signal_strength += cycle * x
            x += int(instruction[1])
    return signal_strength
    
def part2(data):
    instructions = [line.split(" ") for line in data.split("\n")]
    crt_screen = [["." for j in range(0,40)] for i in range(0,6)]
    x = [x for x in range(1, 4)]
    instruction_index = 0
    addx_step = 0
    for cycle in range(0, 240):
        if instructions[instruction_index][0] == "addx":
            addx_step += 1
        elif instructions[instruction_index][0] == "noop":
            instruction_index += 1
        if addx_step == 3:
            addx_step = 1
            x = [x[i] + int(instructions[instruction_index][1]) for i in range(0,3)]
            instruction_index += 1
        crt_screen[int(cycle / 40)][cycle % 40] = "#" if cycle % 40 + 1 in x else "."
    showCrt(crt_screen)
    return 1

with open("input.txt") as f:
    data = f.read()
    
print("1:", part1(data))
print("2: [GRAPHICAL ANSWER BELOW]")
part2(data)