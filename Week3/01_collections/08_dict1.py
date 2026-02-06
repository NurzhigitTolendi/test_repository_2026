# Dictionaries

ourdict = { # furniture_type : price_in_tg
    "table": 15000,
    "chair": 20000,
    "bed": 100,
    "sofa": 0
}

ourdict["closet"] = 50000 

print(ourdict)

ourdict.update({"chair": 30000})

ourdict["bed"] = 1000 # KeyError if key is not present

print(ourdict.get("bed"))
print(ourdict.get("desk")) # None if the key is not present

print(ourdict)

del ourdict["sofa"] # KeyError if key is not present

print(ourdict)