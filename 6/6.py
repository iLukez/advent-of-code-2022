def part1(data):
    windowSize = 4
    window = ()
    for i, _ in enumerate(data):
        window = data[i: i + windowSize]
        for j, c in enumerate(window):
            if (window.count(c) > 1):
                break
            if (j >= windowSize - 1):
                return i + windowSize

def part2(data):
    windowSize = 14
    window = ()
    for i, _ in enumerate(data):
        window = data[i: i + windowSize]
        for j, c in enumerate(window):
            if (window.count(c) > 1):
                break
            if (j >= windowSize - 1):
                return i + windowSize

with open("input.txt") as f:
    data = f.read()
    
print("1:", part1(data))
print("2:", part2(data))