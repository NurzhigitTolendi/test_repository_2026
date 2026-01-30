# Strings

# strings are immutable in python - you cannot change the string directly

a = "cat"

# this gives us an error
# a[0] = "r"

# but we can give a different value to a variable
a = "rat"

print(a)


a = a.replace('c', 'r')
print(a)

# or

a = "cat"
b = 'c'
c = 'r'

a = a.replace(b, c)
print(a)