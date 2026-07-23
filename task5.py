import json
d = json.loads(input('Input dict:'))

def delet0(d):
    do={}
    for key, value in d.items():
        if value != None: do[key]=value
    return do

print(delet0(d))

