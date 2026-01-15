antinodes = []
antennas = {}
row = 0
col = 0


def check_if_in_map(x, y, add_x, add_y, move):
    in_map = False
    if 0 <= x < row and 0 <= y <= col:
        in_map = True
        if [x, y] not in antinodes:
            antinodes.append([x, y])

    if move == "up":
        x -= add_x
        y -= add_y
    else:
        x += add_x
        y += add_y
    if in_map:
        check_if_in_map(x, y, add_x, add_y, move)



while True:
    line = input()
    if line == "stop":
        break

    col = len(line) - 1
    for i in range(len(line)):
        if line[i] != ".":
            if line[i] not in antennas.keys():
                antennas[line[i]] = []

            antennas[line[i]].append([row, i])

    row += 1
    print(antennas)


for antenna_type in antennas.keys():

    if len(antennas[antenna_type]) > 1:
        for i in antennas[antenna_type]:
            if i not in antinodes:
                antinodes.append(i)

    while len(antennas[antenna_type]) > 1:
        first_antenna = antennas[antenna_type].pop(0)
        for second_antenna in antennas[antenna_type]:
            x = second_antenna[0] - first_antenna[0]
            y = second_antenna[1] - first_antenna[1]
            first_antinode = []
            second_antinode = []

            first_antinode.append(first_antenna[0] - x)
            second_antinode.append(second_antenna[0] + x)
            first_antinode.append(first_antenna[1] - y)
            second_antinode.append(second_antenna[1] + y)

            check_if_in_map(first_antinode[0], first_antinode[1], x, y, 'up')
            check_if_in_map(second_antinode[0], second_antinode[1], x, y, 'down')

print(sorted(antinodes))
print(len(antinodes))
