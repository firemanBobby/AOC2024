rules = {}
total = 0

while True:
    rule = input().split("|")
    if rule[0] == "":
        break
    before = "before" + rule[1]
    after = "after" + rule[0]

    if before not in rules.keys():
        rules[before] = [rule[0]]
    elif before in rules.keys():
        rules[before].append(rule[0])

    if after not in rules.keys():
        rules[after] = [rule[1]]
    elif after in rules.keys():
        rules[after].append(rule[1])

while True:
    update = input().split(",")
    passed = []
    correct = True
    if update[0] == "stop":
        break

    for num in range(len(update)):
        x = update.pop(0)
        before = "before" + x
        after = "after" + x
        for passed_num in passed:
            if after in rules:
                if passed_num in rules[after]:
                    correct = False
                    break

        for upcoming_num in update:
            if before in rules:
                if upcoming_num in rules[before]:
                    correct = False
                    break

        passed.append(x)
        if not correct:
            break
    if correct:
        total += int(passed[(len(passed) // 2)])

print(total)
