s=input().split()
o=""
for i in s:
    o+=' '
    o+=i[::-1]
o=o.lstrip()
print(o)

