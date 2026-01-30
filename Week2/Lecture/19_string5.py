# Strings

# string are immutable in python - you cannot change the string directly

a = "cAT"

a.capitalize()

print(a) # Nothing is changed

print(a.capitalize())
print(a) # a is still the same

a = a.capitalize()
print(a) # a is now holding capitalized value