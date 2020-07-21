"""
Takes a price and the amount given and returns a dictionary indicating how
much change should be returned in pennies, nickels, dimes and quarters.  If
the amount given is less than the price an exception will be thrown.  All
values in the dictionary will be integers.
"""


def getChange(price: float, given: float) -> dict:
    reg = {
        "pennies": "pennies",
        "nickels": "nickels",
        "dimes": "dimes",
        "quarters": "quarters",
    }

    if given < price:
        raise Exception("I aint no foo, FOO!!!!")

    given = given * 100
    price = price * 100
    change = given - price

    if change < 25:
        q = 0
    else:
        q = change / 25
        print(q)
        q = int(q) * 100
        change -= q * 0.25
        q /= 100

    if change < 10:
        d = 0
    else:
        d = change / 10
        print(d)
        d = int(d) * 100
        change -= d * 0.1
        d /= 100

    if change < 5:
        n = 0
    else:
        n = change / 5
        print(n)
        n = int(n) * 100
        change -= n * 0.05
        n /= 100

    if change >= 1:
        p = change / 1
        print(p)
        p = int(p) * 100
        change -= p * 0.01
        p /= 100
    else:
        p = 0

    reg["quarters"] = q
    reg["dimes"] = d
    reg["nickels"] = n
    reg["pennies"] = p

    return reg


print(getChange(0.01, 0.06))
