def part1(data):
    score = 0
    for i, line in enumerate(data):
        turn = line.split(" ")
        turn[0] = ord(turn[0]) - 64
        turn[1] = ord(turn[1]) - 87
        score += turn[1]
        if turn[1] == turn[0]:
            score += 3
        diff = turn[1] - turn[0]
        if diff == 1 or diff == -2:
            score += 6
    return score  
            
def part2(data):
    score = 0
    for i, line in enumerate(data):
        turn = line.split(" ")
        turn[0] = ord(turn[0]) - 64
        turn[1] = ord(turn[1]) - 87
        
    return score 

with open("input.txt") as f:
    data = f.read().split("\n")
    
print("1:", part1(data))
print("2:", part2(data))