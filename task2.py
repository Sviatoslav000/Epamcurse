def sumn(n):
    o=0
    for i in str(n):
        o+=int(i)
    return o

n=int(input())
if n<=0:
    print("Error")
else:
    print(sumn(n))
