class Monkey:
    def __init__(self, index, items, operation, test_divisor, index_true_monkey, index_false_monkey):
        self.index = index
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.index_true_monkey = index_true_monkey
        self.index_false_monkey = index_false_monkey
        self.inspected_items = 0
    
    def do_operation1(self, old):
        operand = old if self.operation[1] == "old" else int(self.operation[1])
        return operand + old if self.operation[0] == "+" else operand * old
    
    def do_operation2(self, old):
        operand = old if self.operation[1] == "old" else int(self.operation[1])
        return operand + old if self.operation[0] == "+" else operand * old
    
    def test(self, value):
        if value % self.test_divisor == 0:
            return True
        return False

def part1(data):
    data = [line.strip().split(" ") for line in data.split("\n")]
    monkeys = []
    monkey_items = []
    monkey_test_divisor = 0
    monkey_operation = []
    monkey_index_true_monkey = 0
    monkey_index_false_monkey = 0
    for i in range (0, int((len(data) + 1) / 7)):
        base_index = i * 7
        monkey_index = int(data[base_index][1].replace(":", ""))
        for j in range(2, len(data[base_index + 1])):
            if j == len(data[base_index + 1]) - 1:
                monkey_items.append(int(data[base_index + 1][j]))
            else:
                monkey_items.append(int(data[base_index + 1][j].replace(",", "")))
        monkey_operation.append(data[base_index + 2][4])
        monkey_operation.append(data[base_index + 2][5])
        monkey_test_divisor = int(data[base_index + 3][3])
        monkey_index_true_monkey = int(data[base_index + 4][5])
        monkey_index_false_monkey = int(data[base_index + 5][5])
        monkeys.append(Monkey(monkey_index, monkey_items, monkey_operation, monkey_test_divisor, monkey_index_true_monkey, monkey_index_false_monkey))
        monkey_items = []
        monkey_operation = []
        
    inspected_items = [0 for x in range(0, len(monkeys))]
    for i in range(0, 20):
        for j in range(0, len(monkeys)):
            n_items = len(monkeys[j].items)
            n_inspected = 0
            for k in range(0, n_items):
                n_inspected += 1
                item = monkeys[j].items.pop()
                item = int(monkeys[j].do_operation1(item) / 3)
                throw_index = monkeys[j].index_true_monkey if monkeys[j].test(item) else monkeys[j].index_false_monkey
                monkeys[throw_index].items.append(item)
            inspected_items[j] += n_inspected
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]
    
def part2(data):
    data = [line.strip().split(" ") for line in data.split("\n")]
    monkeys = []
    monkey_items = []
    monkey_test_divisor = 0
    monkey_operation = []
    monkey_index_true_monkey = 0
    monkey_index_false_monkey = 0
    for i in range (0, int((len(data) + 1) / 7)):
        base_index = i * 7
        monkey_index = int(data[base_index][1].replace(":", ""))
        for j in range(2, len(data[base_index + 1])):
            if j == len(data[base_index + 1]) - 1:
                monkey_items.append(int(data[base_index + 1][j]))
            else:
                monkey_items.append(int(data[base_index + 1][j].replace(",", "")))
        monkey_operation.append(data[base_index + 2][4])
        monkey_operation.append(data[base_index + 2][5])
        monkey_test_divisor = int(data[base_index + 3][3])
        monkey_index_true_monkey = int(data[base_index + 4][5])
        monkey_index_false_monkey = int(data[base_index + 5][5])
        monkeys.append(Monkey(monkey_index, monkey_items, monkey_operation, monkey_test_divisor, monkey_index_true_monkey, monkey_index_false_monkey))
        monkey_items = []
        monkey_operation = []
        
    inspected_items = [0 for x in range(0, len(monkeys))]
    for i in range(0, 1000):
        for j in range(0, len(monkeys)):
            n_items = len(monkeys[j].items)
            n_inspected = 0
            for k in range(0, n_items):
                n_inspected += 1
                item = monkeys[j].items.pop()
                item = int(monkeys[j].do_operation2(item))
                throw_index = monkeys[j].index_true_monkey if monkeys[j].test(item) else monkeys[j].index_false_monkey
                monkeys[throw_index].items.append(item)
            inspected_items[j] += n_inspected
        print(i)
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]

with open("input_test.txt") as f:
    data = f.read()
    
print("1:", part1(data))
print("2:", part2(data))