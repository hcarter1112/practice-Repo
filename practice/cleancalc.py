def main():
    repeat = True
    error = True
    option = [1]
    number1 = []
    number2 = []
    operator = []
    answer = []
    while repeat:
        keepGoing = True
        while keepGoing:
            if option[0] == 2:
                keepGoing = False
            else:
                keepGoing = enterNumber1(number1)

        if len(number1) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = enterOperator(operator, number1, option)

        if len(operator) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = enterNumber2(number2)

        if len(number2) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = giveAnswer(number1, number2, operator, answer)

        if len(answer) > 0:
            keepGoing = True
            while keepGoing:
                keepGoing = calcMenu(number1, number2, operator, answer, option)

        if keepGoing == False and option[0] == 2 or option[0] == 1:
            repeat = True

        if keepGoing == False and option[0] == 4:
            repeat = False

    print("The application has closed.")


def enterNumber1(number1):
    haveNumber = True
    while haveNumber:
        number = input("Enter your first number here: ")
        is_number = number.isnumeric()
        if is_number:
            number1.append(number)
            return False
        else:
            print("error")

    if is_number:
        return False


def enterOperator(operator, number1, option):
    haveOperator = True
    while haveOperator:
        if option[0] == 2:
            print("Your previous answer is: " + str(number1[0]))
            op = input(
                "\nInput your operation. H.A.M. 2.0 supports multiplication '*', division '/', subtraction '-', addition '+': "
            )
        else:
            op = input(
                "\nInput your operation. H.A.M. 2.0 supports multiplication '*', division '/', subtraction '-', addition '+': "
            )
        if op == "+" or op == "-" or op == "*" or op == "/":
            operator.append(op)
            return False
        else:
            print("error")

    if len(operator) > 0:
        return False


def enterNumber2(number2):
    haveNumber = True
    while haveNumber:
        number = input("\nEnter your second number here: ")
        is_number = number.isnumeric()
        if is_number:
            number2.append(number)
            return False
        else:
            print("error")

    if len(number2) > 0:
        return False


def giveAnswer(number1, number2, operator, answer):
    if operator[0] == "+":
        ans = float(number1[0]) + float(number2[0])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "-":
        ans = float(number1[0]) - float(number2[0])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "*":
        ans = float(number1[0]) * float(number2[0])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False

    elif operator[0] == "/":
        ans = float(number1[0]) / float(number2[0])
        answer.clear()
        answer.append(ans)
        print("\nYour answer is " + str(ans))
        return False


def calcMenu(number1, number2, operator, answer, option):
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
        number1.clear()
        number2.clear()
        operator.clear()
        answer.clear()
        o = 1
        option.append(o)
        result = False
        return result

    elif choice == "2":
        a = answer[0]
        number1.clear()
        number2.clear()
        operator.clear()
        number1.append(a)
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
