import copy
x = 0
y = 0

r = 0
card = []
direction = 0
directions = ["^", ">", "v", "<"]
obstacles = 0
obstacle = {}

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
next_x = x - 1
next_y = y
card[x][y] = "."
print(x, y)
while 0 <= next_x < len(card) and 0 <= next_y < len(card[0]):

    if card[next_x][next_y] == "#":
        next_y = y
        next_x = x
        direction += 1
        if direction == 4:
            direction = 0
        if direction == 0:
            next_x -= 1

        elif direction == 1:
            next_y += 1

        elif direction == 2:
            next_x += 1

        elif direction == 3:
            next_y -= 1

        continue

    been = []
    if next_x not in obstacle.keys():
        obstacle[next_x] = []
    if card[next_x][next_y] != "#" and next_y not in obstacle[next_x]:
        card_copy = copy.deepcopy(card)
        card_copy[next_x][next_y] = "O"
        obstacle[next_x].append(next_y)

        direction_sim = direction
        x_def = x
        y_def = y
        x_sim = next_x
        y_sim = next_y

        while 0 <= x_sim < len(card) and 0 <= y_sim < len(card[0]):
            if card_copy[x_sim][y_sim] == "#" or card_copy[x_sim][y_sim] == "O":
                x_sim = x_def
                y_sim = y_def
                been.append([x_def, y_def, direction_sim])
                direction_sim += 1
                if direction_sim == 4:
                    direction_sim = 0

                if direction_sim == 0:
                    x_sim -= 1

                elif direction_sim == 1:
                    y_sim += 1

                elif direction_sim == 2:
                    x_sim += 1

                elif direction_sim == 3:
                    y_sim -= 1
                card_copy[x_def][y_def] = "+"
                continue

            if (direction_sim == 0 or direction_sim == 2) and card_copy[x_def][y_def] != "+":
                card_copy[x_def][y_def] = "|"
            elif (direction_sim == 1 or direction_sim == 3) and card_copy[x_def][y_def] != "+":
                card_copy[x_def][y_def] = "-"

            if direction_sim == 0:
                x_sim -= 1
                x_def -= 1

            elif direction_sim == 1:
                y_sim += 1
                y_def += 1

            elif direction_sim == 2:
                x_sim += 1
                x_def += 1

            elif direction_sim == 3:
                y_sim -= 1
                y_def -= 1

            if [x_def, y_def, direction_sim] in been:
                obstacles += 1
                print(x, y)
                card_copy[x][y] = directions[direction]
                # for i in range(len(card)):
                #     print("".join(card_copy[i]))
                # asd = input()
                break

    if direction == 0:
        next_x -= 1
        x -= 1

    elif direction == 1:
        next_y += 1
        y += 1

    elif direction == 2:
        next_x += 1
        x += 1

    elif direction == 3:
        next_y -= 1
        y -= 1

    if not 0 <= next_x < len(card) or not 0 <= next_y < len(card[0]):
        break

print(obstacles)
print(x, y)
