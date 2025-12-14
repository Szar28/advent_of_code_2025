"""
we have to count the clicks now

answers: 
5559: too low
7275: too high
"""
import math

total = 0
dial = 50
dial_key = 100

with open('input.txt') as openfileobject:
    for line in openfileobject:
        line = line.strip()
        s = ""
        n = ""
        for c in line:
            if c.isdigit():
                n += c
            else:
                s += c
        result = 0
        number = int(n)

        # for all the clicks
        clicks = math.floor(number / dial_key)
        print(clicks)
        total += clicks
        crumbs = number % dial_key
        if s == "L":
            if (dial - crumbs) < 0 and dial != 0:
                total += 1
            result = abs(((dial - number) + 1000) % dial_key)
        elif s == "R":
            if (dial + crumbs) > 100 and dial != 100:
                total += 1
            result = abs(((dial + number) + 1000) % dial_key)
        if result == 0:
            total += 1
        dial = result
print(total)
