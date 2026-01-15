total = 0
operators = []


def add(current):
    operators[current] += 1
    while operators[current] == 3:
        operators[current] = 0
        current -= 1
        if current == -1:
            break
        operators[current] += 1



while True:
    equation = input()
    if equation == "stop":
        break
    else:
        equation = equation.split(": ")
        value = int(equation[0])
        col = map(int, equation[1].split())
        col = list(col)

    operators = [0] * (len(col) - 1)
    print(value)
    for iteration in range(3 ** len(operators)):
        print(operators)
        result = col[0]
        flag = False
        for index in range(len(operators)):

            if operators[index] == 0:
                result += col[index + 1]
            elif operators[index] == 1:
                result = result * col[index + 1]
            elif operators[index] == 2:
                result = str(result)
                result += str(col[index + 1])
                result = int(result)

        if result == value:
            flag = True
            total += value
            break

        add(len(operators) - 1)
        if flag:
            break



print(total)



