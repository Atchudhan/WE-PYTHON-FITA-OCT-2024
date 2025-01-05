x="Balaji"


def Myfun():
    x="Sankar"
    print("The Main Don is"," "+x)
Myfun()

print("Supporting Don is"," "+ x)

#Below is the Global keywords used in all

def Myf1():
    global y
y=2
print(y)

Myf1()

print("Here used globally in Outside function",y)
