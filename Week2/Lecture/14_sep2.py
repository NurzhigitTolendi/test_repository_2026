# Output

a = 1
b = 2
c = 3

# sep - string separator between output items
# end - string that is printed at the end of the output, i.e. after all items have been printed

print(a, end = ';\n') # print ends with a semicolon followed by a new line
print(b, end = ';\n')
print(c, end = ';\n')

print(a, b, c, sep = ', ')  # print items are separated with a comma and a space
# by deafult, sep=' ', end='\n'