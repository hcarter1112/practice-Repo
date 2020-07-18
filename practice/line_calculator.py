print('Welcome to Harold\'s More Advanced Calculator, a.k.a "H-MAC". Type "Exit"')
print('at any time to close the app or "Help" for a list of possible operations.')


def main():
    numbers = []
    operator = []
    answer = []
    keepGoing = True

    # help and exit and clear functions are not yet operational. I am just working on getting a better calculator working first.

    while keepGoing:
        keepGoing = number_Entry(numbers)
    if len(numbers) > 0:
        keepGoing = True
        while keepGoing:
            keepGoing = operator_Entry(operator)
    if len(operator) > 0:
        keepGoing = True
        while keepGoing:
            keepGoing = number_Entry(numbers)
    if len(numbers) > 1:
        keepGoing = True
        while keepGoing:
            keepGoing = give_Answer(numbers, operator, answer)
    if len(answer) > 0:
        keepGoing = True
        a = answer[0]
        numbers.clear()
        numbers.append(a)
        keepGoing = main()


# calculator portion works, now I need to get it to be able to loop back through with memory of the previous answer.


def number_Entry(numbers):
    num_value = True
    while num_value:
        number = input()
        is_number = True
        if number == "exit":
            return False
        elif number == "help":
            return False
        elif is_number:
            numbers.append(number)
            num_value = False
        else:
            print("Invalid Entry")
    if len(numbers) > 0:
        return False


def operator_Entry(operator):
    op_value = True
    while op_value:
        op = input()
        if op == "exit":
            return False
        elif op == "help":
            return False
        elif op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "%":
            operator.append(op)
            return False
        else:
            print(
                'Please enter a supported operator or type "Help" for a list of acceptable operations'
            )
            return False
    if len(operator) > 0:
        print("of")
        return False


def give_Answer(numbers, operator, answer):
    if operator[0] == "+":
        ans = float(numbers[0]) + float(numbers[1])
        answer.append(ans)
        print("= " + str(ans))
        return False
    elif operator[0] == "-":
        ans = float(numbers[0]) - float(numbers[1])
        answer.append(ans)
        print("= " + str(ans))
        return False
    elif operator[0] == "*":
        ans = float(numbers[0]) * float(numbers[1])
        answer.append(ans)
        print("= " + str(ans))
        return False
    elif operator[0] == "/":
        ans = float(numbers[0]) / float(numbers[1])
        answer.append(ans)
        print("= " + str(ans))
        return False
    elif operator[0] == "^":
        ans = 1
        for index in range(int(numbers[1])):
            ans = ans * int(numbers[0])
        answer.append(ans)
        print("= " + str(ans))
        return False
    elif operator[0] == "%":
        perc = float(numbers[0]) * 0.01
        ans = perc * float(numbers[1])
        answer.append(ans)
        print("= " + str(ans))
        return False


if __name__ == "__main__":
    main()
