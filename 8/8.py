def part1(data):
    data = data.split("\n")
    tree = [[int(c) for c in line] for line in data]
    visibles = (len(tree) + len(tree[0]) - 1) * 2 - 2
    
    for i, line in enumerate(tree):
        if i == 0 or i == len(tree) - 1: continue
        for j, height in enumerate(line):
            is_visible = False
            if j == 0 or j == len(line) - 1: continue
            # Top
            for top_tree in reversed(range(0, i)):
                if tree[top_tree][j] >= tree[i][j]:
                    break
                elif top_tree == 0:
                    is_visible = True
                    visibles += 1
            if is_visible is True:
                continue
            # Right
            for right_tree in range(j + 1, len(line)):
                if tree[i][right_tree] >= tree[i][j]:
                    break
                elif right_tree == len(line) - 1:
                    is_visible = True
                    visibles += 1
            if is_visible is True:
                continue
            # Bottom
            for bottom_tree in range(i + 1, len(tree)):
                if tree[bottom_tree][j] >= tree[i][j]:
                    break
                elif bottom_tree == len(tree) - 1:
                    is_visible = True
                    visibles += 1
            if is_visible is True:
                continue
            # left
            for left_tree in reversed(range(0, j)):
                if tree[i][left_tree] >= tree[i][j]:
                    break
                elif left_tree == 0:
                    is_visible = True
                    visibles += 1
            if is_visible is True:
                continue
    return visibles
    
def part2(data):
    data = data.split("\n")
    tree = [[int(c) for c in line] for line in data]
    max_scenic_score = 0
    
    for i, line in enumerate(tree):
        if i == 0 or i == len(tree) - 1: continue
        for j, height in enumerate(line):
            is_visible = False
            if j == 0 or j == len(line) - 1: continue
            ss_T = ss_R = ss_B = ss_L = 0
            # Top
            for top_tree in reversed(range(0, i)):
                ss_T += 1
                if tree[top_tree][j] >= tree[i][j]:
                    break
            # Right
            for right_tree in range(j + 1, len(line)):
                ss_R +=1
                if tree[i][right_tree] >= tree[i][j]:
                    break
            # Bottom
            for bottom_tree in range(i + 1, len(tree)):
                ss_B += 1
                if tree[bottom_tree][j] >= tree[i][j]:
                    break
            # left
            for left_tree in reversed(range(0, j)):
                ss_L += 1
                if tree[i][left_tree] >= tree[i][j]:
                    break
            scenic_score = ss_T * ss_R * ss_B * ss_L
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score  
    return max_scenic_score

with open("input.txt") as f:
    data = f.read()
    
print("1:", part1(data))
print("2:", part2(data))