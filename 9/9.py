def findDistance(pos_h, pos_t):
    return max(abs(pos_h[0] - pos_t[0]), abs(pos_h[1] - pos_t[1]))

def move_diagonally(pos_move, pos_reach):
    if pos_reach[0] > pos_move[0] and pos_reach[1] > pos_move[1]:
        pos_move[0] += 1
        pos_move[1] += 1
    if pos_reach[0] < pos_move[0] and pos_reach[1] > pos_move[1]:
        pos_move[0] -= 1
        pos_move[1] += 1
    if pos_reach[0] < pos_move[0] and pos_reach[1] < pos_move[1]:
        pos_move[0] -= 1
        pos_move[1] -= 1
    if pos_reach[0] > pos_move[0] and pos_reach[1] < pos_move[1]:
        pos_move[0] += 1
        pos_move[1] -= 1

def part1(data):
    moves = [tuple(line.split(" ")) for line in data.split("\n")]
    visited_pos = set()
    pos_t = [0, 0]
    pos_h = [0, 0]
    for move in moves:
        for i in range(0, int(move[1])):
            prev_pos_h = pos_h.copy()
            if move[0] == 'U':
                pos_h[1] += 1
            elif move[0] == 'R':
                pos_h[0] += 1
            elif move[0] == 'D':
                pos_h[1] -= 1
            elif move[0] == 'L':
                pos_h[0] -= 1
            if findDistance(pos_t, pos_h) >= 2 and (pos_t[0] == pos_h[0] or pos_t[1] == pos_h[1]):
                pos_t = prev_pos_h
            elif findDistance(pos_t, pos_h) >= 2:
                move_diagonally(pos_t, pos_h)
            visited_pos.add(tuple(pos_t))
    return len(visited_pos)
    
def part2(data):
    moves = [tuple(line.split(" ")) for line in data.split("\n")]
    visited_pos = set()
    pos = [[0, 0] for i in range(0, 10)]
    prev_pos = [[0, 0] for i in range(0, 10)]
    for move in moves:
        for i in range(0, int(move[1])):
            prev_pos[0] = pos[0].copy()
            if move[0] == 'U':
                pos[0][1] += 1
            elif move[0] == 'R':
                pos[0][0] += 1
            elif move[0] == 'D':
                pos[0][1] -= 1
            elif move[0] == 'L':
                pos[0][0] -= 1
            for j in range(1, len(pos)):
                prev_pos[j] = pos[j].copy()
                if findDistance(pos[j - 1], pos[j]) >= 2 and (pos[j-1][0] == pos[j][0] or pos[j-1][1] == pos[j][1]):
                    pos[j] = prev_pos[j-1]
                elif findDistance(pos[j - 1], pos[j]) >= 2:
                    move_diagonally(pos[j], pos[j - 1]) 
            visited_pos.add(tuple(pos[9]))
    return len(visited_pos)

with open("input.txt") as f:
    data = f.read()
    
print("1:", part1(data))
print("2:", part2(data))
print("Solution for Part 2 is currently wrong")