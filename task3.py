def check(s):
    return "yes" if s==s[::-1] else "no"

s=str(input())
print(check(s))
