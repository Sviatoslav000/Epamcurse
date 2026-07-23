with open("foo.txt") as fo:
    s=fo.read()
    print(s)

with open("foo.txt") as fo:
    for line in fo:
        print(line)
