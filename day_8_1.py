antinodes = []
antennas = {}
row = 0
col = 0
city_map = []


def check_if_in_map(x, y):
    if 0 <= x < row and 0 <= y <= col and [x, y] not in antinodes:
        print(x, y)
        antinodes.append([x, y])


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

            check_if_in_map(first_antinode[0], first_antinode[1])
            check_if_in_map(second_antinode[0], second_antinode[1])

print(len(antinodes))