# Functions

x = 1 # global variable

def func():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x)

func()
print(x)