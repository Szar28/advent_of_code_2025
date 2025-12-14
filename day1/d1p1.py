"""
Dial is 0 - 99
Left: minus, right: plus
Ex: Dial = 5, L10 makes dial = 95
Dial starts at 50
Count how many times dial is pointed at 0 after any rotation
"""


total = 0
dial = 50
dial_key = 100

with open('input1.txt') as openfileobject:
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
        if s == "L":
            result = abs(((dial - number) + 1000) % dial_key)
        elif s == "R":
            result = abs(((dial + number) + 1000) % dial_key)
        if result == 0:
            total += 1
        dial = result
print(total)
