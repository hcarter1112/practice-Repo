def main():
    repeat = True
    error = True
    option = [1]
    numbers = []
    operator = []
    answer = []
    while repeat:
        keepGoing = True
        while keepGoing:
            if option[0] == 2:
                keepGoing = False
            else:
                keepGoing = enterNumber1(numbers)

        if len(numbers) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = enterOperator(operator, numbers, option)

        if len(operator) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = enterNumber2(numbers)

        if len(numbers) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = giveAnswer(numbers, operator, answer)

        if len(answer) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = calcMenu(numbers, operator, answer, option)

        if keepGoing == False and option[0] == 2 or option[0] == 1:
            repeat = True

        if keepGoing == False and option[0] == 4:
            repeat = False

    print("The application has closed.")


def enterNumber1(numbers):
    haveNumber = True
    while haveNumber:
        number = input("Enter your first number here: ")
        is_number = number.isnumeric()
        if is_number:
            numbers.append(number)
            return False
        else:
            print("error")

    if is_number:
        return False


def enterOperator(operator, numbers, option):
    haveOperator = True
    while haveOperator:
        if option[0] == 2:
            print("Your previous answer is: " + str(numbers[0]))
            op = input(
                "\nInput your operation. H.A.M. 2.0 supports multiplication '*', division '/', subtraction '-', addition '+', exponents '^'(experimental- intergers only): "
            )
        else:
            op = input(
                "\nInput your operation. H.A.M. 2.0 supports multiplication '*', division '/', subtraction '-', addition '+', exponents '^'(experimental- intergers only): "
            )
        if op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
            operator.append(op)
            return False
        else:
            print("error")

    if len(operator) > 0:
        return False


def enterNumber2(numbers):
    haveNumber = True
    while haveNumber:
        number = input("\nEnter your second number here: ")
        is_number = number.isnumeric()
        if is_number:
            numbers.append(number)
            return False
        else:
            print("error")

    if len(numbers) > 0:
        return False


def giveAnswer(numbers, operator, answer):
    if operator[0] == "+":
        ans = float(numbers[0]) + float(numbers[1])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "-":
        ans = float(numbers[0]) - float(numbers[1])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "*":
        ans = float(numbers[0]) * float(numbers[1])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "/":
        ans = float(numbers[0]) / float(numbers[1])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "^":
        ans = 1
        for index in range(int(numbers[1])):
            ans = ans * int(numbers[0])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False


def calcMenu(numbers, operator, answer, option):
    result = True
    option.clear()
    menu = [
        "\n1. Clear the calculator and start from the beginning",
        "2. Continue operations with this number ",
        "3. repeat your answer",
        "4. Exit the application",
        "\nPlease select an option: ",
    ]
    choice = input("\n".join(menu)).strip()
    print()

    if choice == "1":
        numbers.clear()
        numbers.clear()
        operator.clear()
        answer.clear()
        o = 1
        option.append(o)
        result = False
        return result

    elif choice == "2":
        a = answer[0]
        numbers.clear()
        numbers.clear()
        operator.clear()
        numbers.append(a)
        o = 2
        option.append(o)

        result = False
        return result

    elif choice == "3":
        print("Your answer is: " + str(answer[0]))
        result = True

        return result

    elif choice == "4":
        o = 4
        option.append(o)
        result = False
        return result

    else:
        print("error")
        result = True
        return result


if __name__ == "__main__":
    main()
