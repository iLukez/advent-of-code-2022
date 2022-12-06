def part1(data):
    elfs = []
    calories = 0
    for line in data:
        if (line == ""):
            elfs.append(calories)
            calories = 0
            continue
        calories += int(line)
    return max(elfs)
    
def part2(data):
    elfs = []
    calories = 0
    for line in data:
        if (line == ""):
            elfs.append(calories)
            calories = 0
            continue
        calories += int(line)
    max_sum = max(elfs)
    elfs.remove(max(elfs))
    max_sum += max(elfs)
    elfs.remove(max(elfs))
    max_sum += max(elfs)
    elfs.remove(max(elfs))
    return max_sum

with open("input.txt") as f:
    data = f.read().split("\n")
    
print("1:", part1(data))
print("2:", part2(data))