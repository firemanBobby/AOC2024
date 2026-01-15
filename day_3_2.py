import re

total = 0
line = ''
while True:

    a = input()
    if a == 'stop':
        break
    else:
        line += a


text = re.sub(r"don't[(][)].*?(do[(][)]?)|don't[(][)].*$", "", line)

found = re.findall(r"[m][u][l][(](\d+),(\d+)[)]", text)

for i in range(len(found)):
    total += int(found[i][0]) * int(found[i][1])
    print(found[i])
print(total)