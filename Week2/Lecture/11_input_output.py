# Input and output

# Input

a = int(input()) # to get a specific type, type cast the input 
print(a)
print(type(a))

a = float(input())
print(a)
print(type(a))

a = bool(input()) # input nothing to get false
print(a)          # or anything else to get true
print(type(a))

a = bool(int(input())) # input 0 to get false
print(a)               # or any other integer to get true
print(type(a))