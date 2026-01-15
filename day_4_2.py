sheet = []
counter = 0

while True:
    line = input()
    if line == 'stop':
        break

    sheet.append(line)


for i in range(1, len(sheet) - 1):
    for j in range(1, len(sheet[0]) - 1):
        chars = []
        if sheet[i][j] == "A":
            chars.append(sheet[i - 1][j - 1])
            chars.append(sheet[i - 1][j + 1])
            chars.append(sheet[i + 1][j - 1])
            chars.append(sheet[i + 1][j + 1])
            if "A" in chars or "X" in chars:
                continue

            elif chars.count("M") == 2 and sheet[i - 1][j - 1] != sheet[i + 1][j + 1]:
                counter += 1

print(counter)
