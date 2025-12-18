"""
same rules but if pattern repeats twice
ex: 212121, 123123123
invalid IDs
"""

def duplicate(s: str):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

total = 0
with open("input2.txt") as f:
    for line in f:
        result = [x.strip() for x in line.split(',')]
        for sequence in result:
            if not sequence:
                continue
            lower_end, upper_end = map(int, sequence.split('-'))
            for x in range(lower_end, upper_end+1):
                front = str(x)
                tester = duplicate(front)
                front = front[:len(front)//2]
                back = str(x)
                back = back[len(back)//2:] 
                if front == back or tester:
                    total += x
print(total)
