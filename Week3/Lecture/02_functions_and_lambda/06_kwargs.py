# Functions

# arbitrary keyword arguments, **kwargs
def func(**kwargs):
    print(kwargs) # kwargs is a dict
    for key in kwargs:
        print(key, kwargs[key])

func(phone = "Xiaomi", model = "Redmi Note 15")