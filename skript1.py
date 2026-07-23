def change(mylist):
    mylist.append([1,2,3])
    print("inside funktion:", mylist)

mylist1 = [10,20,30]
change(mylist1)
print("outside", mylist1)
