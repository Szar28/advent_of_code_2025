with open("test.txt") as f:
    for line in f:
        result = [x.strip() for x in line.split(',')]
        print(result)
