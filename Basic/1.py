import time
#import ModuleDemo
from ModuleDemo import print_function

def getNameLength(name):
    return len(name)

def myDictionary():
    mydict = {"1001":"Mike Tyson", "1002": "David Beckham", 1003: "Jackie Chan"}
    print (mydict[1003])

name = "Rachait"
if name=="Rachit":
    print ("Name is Rachit")
else:
    print ("Somebody else")

for n in name:
    print (n)

# del name
print (name[0:4])

fruits = ["apple", "banana", "grapes", ["blackberry","strawberry","rasberry"]]
for fruit in fruits:
    if type(fruit) is list:
        for f in fruit:
            print ("---", f)
    print ("-",type(fruit), fruit)

print (getNameLength("Hackathon"))
myDictionary()
print (time.localtime(time.time()))
print_function("Sushmita")
''' answer = input("Whats your name")
print("Response is " + answer) '''

''' File Operation
txt = open("c:/rachit/demo.txt", "r")
print (txt.name)
print (txt.read(10))
txt.close()
'''
lst = [10, 3, 5, 6]
print (max(lst))

x = lambda a,b,c : a * b * c
print (x(2,3,4))

t1 = ("Rachit", "Nitin", "Adhir")
t2 = ("Kohli", "Ghag", "More")
tzip = zip(t1, t2)
print (tuple(tzip))

