"""
Our goal is to produce the factorial of a variable. e.g. fac 5= 5*4*3*2*1
"""


def factorial_Sequential(fac_num: int) -> int:
    if fac_num < 0:
        raise Exception("Must be < or = 0")
    elif fac_num == 0:
        return 1
    else:
        result = 1
        for index in range(fac_num):
            result = (index + 1) * result
        return result


print(factorial_Sequential(125))
