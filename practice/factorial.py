"""
Our goal is to produce the factorial of a variable. e.g. fac 5= 5*4*3*2*1
"""
import sys

# def factorial_Sequential(fac_num: int) -> int:
#     if fac_num < 0:
#         raise Exception("Must be < or = 0")
#     elif fac_num == 0:
#         return 1
#     else:
#         result = 1
#         for index in range(fac_num):
#             result = (index + 1) * result
#         return result


# print(factorial_Sequential(125))


def recursive(fac_num: int) -> list:
    results = []
    numbers = []
    if fac_num < 0:
        raise Exception("Must be < or = 0")
    if fac_num <= 1:
        return [1]
    a = recursive(fac_num - 1) * fac_num
    x = a[0] * fac_num
    results.append(a[0])
    numbers.append(x)
    return numbers


# recursive(3) = [recursive(2) * 3]


print(recursive(3))
# print()

# 6
# 5
# 4
# 3
# 2
# 1

