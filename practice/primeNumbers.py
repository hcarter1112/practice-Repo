import math


def getPrimesUpTo(num_nums: int) -> list:
    numbers = list(range(1, (num_nums + 1)))
    prime_Numbers = [2]
    if num_nums < 2:
        raise Exception("Please enter a number greater than 1")
    if num_nums == 2:
        return prime_Numbers
    if num_nums == 3:
        prime_Numbers.append(3)
        return prime_Numbers

    i = 3
    while i < num_nums:
        rtnumber = int(math.sqrt(numbers[i]))
        while rtnumber > 1 and i < num_nums:
            if numbers[i] % rtnumber != 0:
                if rtnumber == 2:
                    num = numbers[i]
                    prime_Numbers.append(num)
                    i += 1
                rtnumber -= 1
            else:
                i += 1
                break

    return prime_Numbers


print(getPrimesUpTo(1000000))
