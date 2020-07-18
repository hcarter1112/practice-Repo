def fibonacci_Number(limit: int):
    """
    This function expects an interget that will act as the limit of the output
    go through the sequence until you find the closest number to the given x
    """
    y = 1
    x = 0
    while limit > y:
        x, y = y, x + y
    return x


def fibonacci_List(limit: int) -> list:
    y = 1
    x = 0
    fib_num = [0]
    while limit > y:
        x, y = y, x + y
        # fib_num.append(x)
        fib_num.append(x)
    return fib_num


# 0, 1, 1, 2, 3, 5,

print(fibonacci_List(888880))
