def command(n):
    list=[]
    for i in range(n):
        com=input().split()
        if com[0]=="insert":
            list.insert(int(com[1]),int(com[2]))
        elif com[0]=="print":
            print(list)
        elif com[0]=="remove":
            list.remove(int(com[1]))
        elif com[0]=="append":
            list.append(int(com[1]))
        elif com[0]=="sort":
            list.sort()
        elif com[0]=="pop":
            list.pop()
        elif com[0]=="reverse":
            list.reverse()

n=int(input())
command(n)
