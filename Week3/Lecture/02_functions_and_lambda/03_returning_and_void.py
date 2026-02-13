# Functions

def func1(num1, num2):
    print(num1 + num2)

def func2(num1, num2):
    return num1 + num2

func1(2, 3) # result is 5
func2(2, 3) # returns nothing

print(func2(4, 5)) # 9
print(func1(6, 7)) # 13 and then None on the next line because func1 doesn't have return 