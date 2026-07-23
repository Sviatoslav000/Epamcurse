
def factorial(n):
    i=1
    o=1
    while i<=n:
        o*=i
        i+=1
    return o

n=int(input())
if n<0:
    print("Error")
else:
    print(factorial(n))
