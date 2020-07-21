reg = {
    "pennies": "pennies",
    "nickels": "nickels",
    "dimes": "dimes",
    "quarters": "quarters",
}
change = float(0.01) * 100


if change < 25:
    q = 0
else:
    q = change / 0.25
    q = int(q) * 100
    change = (change * 100) - (q * 0.25)
    q /= 100

if change < 10:
    d = 0
else:
    d = change / 10
    d = int(d) * 100
    change -= d * 0.1
    d /= 100

if change < 5:
    n = 0
else:
    n = change / 5
    n = int(n) * 100
    change -= n * 0.05
    n /= 100

if change >= 1:
    p = change / 1
    p = int(p) * 100
    change -= p * 0.01
    p /= 100
else:
    p = 0

    reg["quarters"] = q
    reg["dimes"] = d
    reg["nickels"] = n
    reg["pennies"] = p
print(p)
