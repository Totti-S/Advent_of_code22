from collections import deque
from math import floor
from time import perf_counter
from numpy import square

def main():
    with open("data/day11_data.txt", "r") as f:
        data = f.read()

    class Item():
        #   13  17  19  23
        dividers = [2,3,5,7,11,13,17,19,23]
        def __init__(self, number):
            self.reminders = [number%num for num in Item.dividers]

    class Monkey():
        def __init__(self, items, operation, div_test, true_idx, false_idx):
            self.items = items
            self.operation = eval('lambda old: ' + operation) # Credit for reminding me about eval function: Brian Chen solution
            self.div_test = int(div_test)
            self.if_true = int(true_idx)
            self.if_false = int(false_idx)
            self.looked_items = 0

        def do(self):
            if self.items:
                for item in self.items:
                    item.reminders = [self.operation(num) % divider for num,divider in zip(item.reminders, Item.dividers)]
                    rem_idx = Item.dividers.index(self.div_test)
                    idx = self.if_false if item.reminders[rem_idx] % self.div_test else self.if_true
                    monkeys[idx].items.append(item)

                self.looked_items += len(self.items)
                self.items = []

    monkeys_data = data.split("\n\n")
    monkeys = []

    for monkey_data in monkeys_data:
        info = monkey_data.split("\n")
        init_info = []
        for i, tmp_info in enumerate(info):
            info_field = tmp_info.strip()
            if i == 1:
                tmp = info_field.split(":")[1].split(",")
                items = [Item(int(i)) for i in tmp]
                init_info.append(items)
            elif i == 2:
                operation_string = info_field.split("=")[-1]
                init_info.append(operation_string.strip())
            elif i > 2:
                list_things = info_field.split(" ")
                init_info.append(list_things[-1])

        monkeys.append(Monkey(*init_info))

    num_rounds = 10_000
    for r in range(0,num_rounds):
        print(r)
        for monkey in monkeys:
            monkey.do()

    inspected_item_counts = sorted([monkey.looked_items for monkey in monkeys])

    print(inspected_item_counts[-1]* inspected_item_counts[-2])

if __name__ == "__main__":
    main()