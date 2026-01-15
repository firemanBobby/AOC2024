x = 0
y = 0
r = 0
card = []
direction = 0
directions = ["^", ">", "v", "<"]
steps = 0

while True:
    line = input()
    if line == "stop":
        break

    row = []
    for i in range(len(line)):
        row.append(line[i])

    card.append(row)
    for i in range(len(row)):
        if row[i] not in [".", "#"]:
            y = i
            x = r
    r += 1

print(len(card))

while True:

    if card[x][y] != "X":
        card[x][y] = "X"
        steps += 1
    # print(x, y)
    # print(steps)

    if direction == 0:
        if x - 1 < 0:
            break
        elif card[x - 1][y] == "#":
            direction += 1
        else:
            x -= 1

    elif direction == 1:
        if y + 1 == len(card[0]):
            break
        elif card[x][y + 1] == "#":
            direction += 1
        else:
            y += 1

    elif direction == 2:
        if x + 1 == len(card):
            break
        elif card[x + 1][y] == "#":
            direction += 1
        else:
            x += 1

    elif direction == 3:
        if y - 1 < 0:
            break
        elif card[x][y - 1] == "#":
            direction += 1
        else:
            y -= 1

    if direction == 4:
        direction = 0

#     for i in range(len(card)):
#         print("".join(card[i]))
#
#     asd = input()
#
#
for i in range(len(card)):
    print("".join(card[i]))
print(x, y)
print(steps)
