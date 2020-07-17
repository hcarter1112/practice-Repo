
answer = True
op = input()
a = 0


while answer:
    print("Enter a number to add to " + str(a) + " (or type \"Done\" to finish)")
    b = input().strip().lower()
    if b == 'done':
        answer = False
    else:
        a = a + float(b)
    

print("Your answer is " + str(a))
