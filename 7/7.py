
class Tree:
    def __init__(self, type, name, size, parent=None):
        self.type = type # 0 = file, 1 = dir
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        
    def getSize(self):
        size = 0
        for child in self.children:
            size += child.size
        return size

    def findChild(self, name):
        for c in self.children:
            if c.name == name: return c

# Directories are always initialized with size = 0. This function sets sizes of directories as the sum of the sizes of their childs 
def setDirsSize(tree):
    size = 0
    for child in tree.children:
        if child.type == 1:
            setDirsSize(child)
        size += child.size
    tree.size = size

# Iterates over all nodes of the tree and if the node is a directory and has size <= 100.000, sums its size to the result
def sum_deletable_dirs(tree, result):
    for child in tree.children:
        if child.type == 1:
            if child.size <= 100_000:
                result += child.size
            result = sum_deletable_dirs(child, result)
    return result

# Iterates over all nodes of the tree and saves in the list dirSize every deletable directory (size >= minimumSize)
def deletable_nodes(tree, minimumSize, dirSize):
    for child in tree.children:
        if child.type == 1:
            if child.size >= minimumSize:
                dirSize.append(child.size)
            deletable_nodes(child, minimumSize, dirSize)

def part1(data):
    data = data.split("\n")
    root = Tree(1, "/", 0)
    currentNode = root
    data = data[1:]
    isLs = False
    for i, line in enumerate(data):
        line = line.split(" ")
        if isLs:
            if line[0] == "dir":
                currentNode.children.append(Tree(1, line[1], 0, currentNode))
            else:
                currentNode.children.append(Tree(0, line[1], int(line[0]), currentNode))
            if i + 1 < len(data) and data[i + 1][0] == "$":
                isLs = False
        elif line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    currentNode = currentNode.parent
                else:
                    currentNode = currentNode.findChild(line[2])
            elif line[1] == "ls":
                isLs = True
    
    setDirsSize(root)
    return sum_deletable_dirs(root, 0)
    
def part2(data):
    data = data.split("\n")
    root = Tree(1, "/", 0)
    currentNode = root
    data = data[1:]
    isLs = False
    for i, line in enumerate(data):
        line = line.split(" ")
        if isLs:
            if line[0] == "dir":
                currentNode.children.append(Tree(1, line[1], 0, currentNode))
            else:
                currentNode.children.append(Tree(0, line[1], int(line[0]), currentNode))
            if i + 1 < len(data) and data[i + 1][0] == "$":
                isLs = False
        elif line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    currentNode = currentNode.parent
                else:
                    currentNode = currentNode.findChild(line[2])
            elif line[1] == "ls":
                isLs = True
    
    setDirsSize(root)
    dirSize = []
    minimumSize = 30_000_000 - (70_000_000 - root.size)
    deletable_nodes(root, minimumSize, dirSize)
    dirSize.sort()
    return dirSize[0]

with open("input.txt") as f:
    data = f.read()

print("1:", part1(data))
print("2:", part2(data))