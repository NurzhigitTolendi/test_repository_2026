# Casting into bool

# Examples of how values are casted into bool
print(bool(1))   # True
print(bool(0))   # False
print(bool(-1))  # True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool(''))  # empty str -> False
print(bool('0')) # True
print(bool([]))  # empty collection -> False
print(bool({}))  # empty collection -> False