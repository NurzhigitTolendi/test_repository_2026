# Dictionaries

ourdict = { # furniture_type : price_in_tg
    "table": 15000,
    "ikea_chair": 20000,
    "bed": 100,
    "sofa": 0
}

for key in ourdict:                  # iterate over keys of the dictionary
    print(key, ourdict[key]) 

for value in ourdict.values():       # iterate over values of the dictionary
    print(value)

for key, value in ourdict.items():   # iterate over items (key, value) of the dictionary
    print(key, value)