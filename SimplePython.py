myInt = 5
myString = "Hello World!"
myFloat = 3.14
print("My integer is {}, my string is {}, and my float is {}".format(myInt, myString, myFloat))

var1 = 4
var2 = 2
plus = var1 + var2
minus = var1 - var2
mult = var1 * var2
div = var1 / var2
var1 += 1
var2 += 2
var3 = var1 % var2
if var1 == var2 and var2 == var3:
    print("Variables 1, 2, and 3 are all equivalent")
elif var1 == var2 or var2 == var3:
    print("Variable 2 is equal to one or both of variable 1 and variable 3")
elif var1 != var2:
    print("Variable 1 is not equal to variable 2")
else:
    print("Variable is {}, variable 2 is {}, and variable is {}".format(var1, var2, var3))

while var3 < 10:
    var3 += 2
    print(var3)

for x in range(0, 3):
    print("x = {}".format(x))

myList = ["Bob", "Joe", "Dan", "Ren", "Han"]
for name in myList:
    print(name)

fibonacciTuple = (1, 1, 2, 3, 5, 8, 13, 21)
for num in fibonacciTuple:
    print(num)

def createString():
    string1 = "I like pie"
    return string1

string2 = createString()
print(string2)
