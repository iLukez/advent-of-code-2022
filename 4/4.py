def isOverlapped(turns):
    if (turns[0][0] <= turns[1][1] and turns[1][0] <= turns[0][0]) or (turns[1][0] <= turns[0][1] and turns[0][0] <= turns[1][0]):
        return True
    return False

def isContained(turns):
    if (turns[1][0] <= turns[0][0] <= turns[0][1] <= turns[1][1] or turns[0][0] <= turns[1][0] <= turns[1][1] <= turns[0][1]):
        return True
    return False

with open('input.txt') as f:
    result1 = 0
    result2 = 0
    data = f.read()
    extractedData = []
    lines = data.split("\n")
    for index, line in enumerate(lines):
        pairs = line.split(",")
        hours1 = pairs[0].split("-")
        hours2 = pairs[1].split("-")
        extractedData.append(((int(hours1[0]), int(hours1[1])), (int(hours2[0]), int(hours2[1]))))
        if (isContained(extractedData[index])):
            result1 += 1
        if isOverlapped(extractedData[index]):
            result2 += 1

print("1:", result1)
print("1:", result2)
