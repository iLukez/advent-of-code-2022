import copy

with open("input.txt") as f:
    data = f.read()
    lines = data.split("\n")
    stacks = [[], [], [], [], [], [], [], [], []]
    stacksLines = []
    instructionLines = []
    for i, line in enumerate(lines):
        if lines[i] == "":
            instructionLines = lines[(i+1):]
            break
        stacksLines.append(lines[i])
    stacksLines.pop()
    stacksData = stacksLines[::-1]
    bufferChars = ""
    counter = 0
    for stacksLine in stacksData:
        for j, char in enumerate(stacksLine):
            if j % 4 == 1:
                if char != " ":
                    stacks[int(j/4)].append(char)

stacks1 = copy.deepcopy(stacks)
stacks2 = copy.deepcopy(stacks)

# Part 1

for line in instructionLines:
    lineList = line.split(" ")
    nCrates = int(lineList[1])
    indexFrom = int(lineList[3]) - 1
    indexTo = int(lineList[5]) - 1
    for i in range(nCrates):
        stacks1[indexTo].append(stacks1[indexFrom].pop())

for stack in stacks1:
    stack.reverse()
    print(stack[0], end="")
print()

# Part 2
for line in instructionLines:
    lineList = line.split(" ")
    nCrates = int(lineList[1])
    indexFrom = int(lineList[3]) - 1
    indexTo = int(lineList[5]) - 1
    buffer = []
    for j in range(nCrates):
        buffer.append(stacks2[indexFrom].pop())
    buffer = buffer[::-1]
    stacks2[indexTo].extend(buffer)

for stack in stacks2:
        stack.reverse()
        print(stack[0], end="")