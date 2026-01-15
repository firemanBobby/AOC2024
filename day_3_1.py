import re

total = 0
while True:
    text = input()
    found = re.findall(r"[m][u][l][(](\d+),(\d+)[)]", text)
    print(found)
    for i in range(len(found)):
        total += int(found[i][0]) * int(found[i][1])
    if text == 'stop':
        break
print(total)
