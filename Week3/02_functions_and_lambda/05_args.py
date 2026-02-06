# Functions

# arbitrary arguments, *args
def func(*args):
    print(args)
    for arg in args:
        print(arg)

func(1, 2, 3)
func(1, 2, 3, "Iron Man suit", "Quinjet", "Black Widow bike", "whatever")