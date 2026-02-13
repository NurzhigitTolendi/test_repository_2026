# Tuples 

ourtuple = ("Say my name", "I did it for me, I felt myself alive", 2008, 
            "Better call Saul", "My name is Gustavo, but you can call me Gus")  # 
 
print(ourtuple)

Heisenberg, Walter, year, Saul, Gus = ourtuple

print(Heisenberg)
print(Walter)
print(year)
print(Saul)
print(Gus)

print(type(ourtuple))

# tuples are immutable 
my_tuples = (1, 2, 3)
# my_tuples[0] = 5 # Error: 'tuple' object does not support item assignment 

# tuples are faster than lists

ourtup = ("Batman", "Wonder Woman", "Superman")

if "Lex Luthor" in ourtup:
    print("Lex is here!")
else:
    print("Lex is not here, he is hiding")

if "Homelander" not in ourtup:
    print("Happily, not found!")
elif "Void" not in ourtup:
    print("He's not here, he's inside of Sentry!")
else:
    print("There're here! Run!")

