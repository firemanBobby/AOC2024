sheet = []
counter = 0

while True:
    line = input()
    if line == 'stop':
        break

    sheet.append(line)

for i in range(len(sheet)):
    for j in range(len(sheet[0])):
        if i < len(sheet) - 3:
            if j < 3:
                if sheet[i][j] == 'X':
                    if sheet[i][j + 1] == 'M' and sheet[i][j + 2] == 'A' and sheet[i][j + 3] == 'S':
                        counter += 1
                    if sheet[i + 1][j + 1] == 'M' and sheet[i + 2][j + 2] == 'A' and sheet[i + 3][j + 3] == 'S':
                        counter += 1
                    if sheet[i + 1][j] == 'M' and sheet[i + 2][j] == 'A' and sheet[i + 3][j] == 'S':
                        counter += 1
                elif sheet[i][j] == 'S':
                    if sheet[i][j + 1] == 'A' and sheet[i][j + 2] == 'M' and sheet[i][j + 3] == 'X':
                        counter += 1
                    if sheet[i + 1][j + 1] == 'A' and sheet[i + 2][j + 2] == 'M' and sheet[i + 3][j + 3] == 'X':
                        counter += 1
                    if sheet[i + 1][j] == 'A' and sheet[i + 2][j] == 'M' and sheet[i + 3][j] == 'X':
                        counter += 1
            elif 3 <= j < len(sheet[0]) - 3:
                if sheet[i][j] == 'X':
                    if sheet[i][j + 1] == 'M' and sheet[i][j + 2] == 'A' and sheet[i][j + 3] == 'S':
                        counter += 1
                    if sheet[i + 1][j + 1] == 'M' and sheet[i + 2][j + 2] == 'A' and sheet[i + 3][j + 3] == 'S':
                        counter += 1
                    if sheet[i + 1][j] == 'M' and sheet[i + 2][j] == 'A' and sheet[i + 3][j] == 'S':
                        counter += 1
                    if sheet[i + 1][j - 1] == 'M' and sheet[i + 2][j - 2] == 'A' and sheet[i + 3][j - 3] == 'S':
                        counter += 1
                elif sheet[i][j] == 'S':
                    if sheet[i][j + 1] == 'A' and sheet[i][j + 2] == 'M' and sheet[i][j + 3] == 'X':
                        counter += 1
                    if sheet[i + 1][j + 1] == 'A' and sheet[i + 2][j + 2] == 'M' and sheet[i + 3][j + 3] == 'X':
                        counter += 1
                    if sheet[i + 1][j] == 'A' and sheet[i + 2][j] == 'M' and sheet[i + 3][j] == 'X':
                        counter += 1
                    if sheet[i + 1][j - 1] == 'A' and sheet[i + 2][j - 2] == 'M' and sheet[i + 3][j - 3] == 'X':
                        counter += 1
            else:
                if sheet[i][j] == 'X':
                    if sheet[i + 1][j] == 'M' and sheet[i + 2][j] == 'A' and sheet[i + 3][j] == 'S':
                        counter += 1
                    if sheet[i + 1][j - 1] == 'M' and sheet[i + 2][j - 2] == 'A' and sheet[i + 3][j - 3] == 'S':
                        counter += 1
                elif sheet[i][j] == 'S':
                    if sheet[i + 1][j] == 'A' and sheet[i + 2][j] == 'M' and sheet[i + 3][j] == 'X':
                        counter += 1
                    if sheet[i + 1][j - 1] == 'A' and sheet[i + 2][j - 2] == 'M' and sheet[i + 3][j - 3] == 'X':
                        counter += 1
        else:
            if j < len(sheet[0]) - 3:
                if sheet[i][j] == 'X':
                    if sheet[i][j + 1] == 'M' and sheet[i][j + 2] == 'A' and sheet[i][j + 3] == 'S':
                        counter += 1
                elif sheet[i][j] == 'S':
                    if sheet[i][j + 1] == 'A' and sheet[i][j + 2] == 'M' and sheet[i][j + 3] == 'X':
                        counter += 1
print(counter)