import csv
with open('femto.txt','r')as e:
    print(e.readlines())

d=['1,2,3,4,5,6,6,6']
with open('femto.txt','a')as b:
    print(b.writelines(d))
with open('femto.txt','r')as k:
    #next(k)
    print(k.readlines())



