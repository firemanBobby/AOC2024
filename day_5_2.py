rules = {}
total = 0

while True:
    rule = input().split("|")
    if rule[0] == "":
        break
    before = "before" + rule[1]

    if before not in rules.keys():
        rules[before] = [rule[0]]
    elif before in rules.keys():
        rules[before].append(rule[0])

while True:
    update = input().split(",")
    correct = True
    if update[0] == "stop":
        break

    for num in range(len(update)):
        x = update[num]
        before = "before" + x

        for upcoming_num in range(num, len(update)):
            if before in rules:
                if update[upcoming_num] in rules[before]:
                    correct = False
                    break

        if not correct:
            break

    if not correct:
        num = 0
        while num < len(update):
            x = update[num]
            before = "before" + x
            for upcoming_num in range(num, len(update)):
                if before in rules:
                    if update[upcoming_num] in rules[before]:
                        update[num], update[upcoming_num] = update[upcoming_num], update[num]
                        num -= 1
                        break
            num += 1

        print(update)
        total += int(update[(len(update) // 2)])
        print(int(update[(len(update) // 2)]))


print(total)
