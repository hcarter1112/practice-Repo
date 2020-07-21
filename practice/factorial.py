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
    if fac_num < 0:
        raise Exception("Must be < or = 0")
    if fac_num <= 1:
        return [1, [1]]
    a, x = recursive(fac_num - 1)
    print(a, x)
    a *= fac_num
    return [a, [a] + x]


print(recursive(5))


# def factorial(facnum: int) -> tuple:
#     if facnum < 0:
#         raise Exception("nah man!")
#     if facnum <= 1:
#         return [1, [1]]
#     result, f_values = factorial(facnum - 1)
#     result *= facnum
#     return [result, [result] + f_values]


# print(factorial(5))


# recursive(3) = [recursive(2) * 3]


# print()

# 6
# 5
# 4
# 3
# 2
# 1

