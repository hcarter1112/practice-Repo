beginning = True
while beginning:
    num1 = True
    while num1:
        print("Input your first number: ")
        a = input().strip()
        letter = a.isalpha()
        if letter:
            print('Invalid entry')
        else:
            num1 = False
    cont = True
    while cont:
        num2 = True
        while num2:
            op = input("Input your operation. H.A.M. 2.0 supports multiplication '*', division '/', subtraction '-', addition '+', and exponents '^':\n")

            if op == "+":
                print("please enter the number you wish to ADD to " + str(a))
                b = input()
                a = float(a) + float(b)
                print("Your answer is: " + str(a))
                num2 = False
            elif op == "-":
                print("please enter the number you wish to SUBTRACT from " + str(a))
                b = input()
                a = float(a) - float(b)
                print("Your answer is: " + str(a))
                num2 = False

            elif op == "*":
                print("please enter the number you wish to MULTIPLY " + str(a) + " by.")
                b = input()
                a = float(a) * float(b)
                print("Your answer is: " + str(a))
                num2 = False

            elif op == "/":
                print("please enter the number you wish to DIVIDE " + str(a) + " by.")
                b = input()
                a = float(a) / float(b)
                print("Your answer is: " + str(a))
                num2 = False

            elif op == "^":
                print(str(a) + " to the power of: ")
                b = input()
                a = float(a) ** float(b)
                print("Your answer is: " + str(a))
                num2 = False

            else:
                print("Invalid")

        menu = True
        while menu:
            print()
            print("Please select your next action")
            print("Type 'CLEAR' to clear the calculator and start from the beginning")
            print("type 'NEXT' to continue operations with this number")
            print("Type 'ANS' repeat your final answer")
            print("Type 'CLOSE' to close the app")
        
            next_op = input().strip().upper()
        
            if next_op == 'CLEAR':
                menu = False
                cont = False
            elif next_op == 'NEXT':
                menu = False
            elif next_op == 'CLOSE':
                menu = False
                cont = False
                beginning = False
            elif next_op == 'ANS':
                print()
                print("Your answer is: " + str(a)) 
            else:
                print("Invalid Entry")


print("You have closed the application. Thank you for using H.A.M. 2.0!")

        