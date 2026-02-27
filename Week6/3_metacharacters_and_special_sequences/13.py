# character classes: [] ranges and negation

import re

text = "Hello World! Today is 17/02/2025. Call +7-555-123-4567. Price: $19.99"

# [a-z] - lowercase letters only
print(re.findall(r"[a-z]+", text))

# [A-Z] - uppercase letters only
print(re.findall(r"[A-Z]+", text))

# [a-zA-Z] - all letters
print(re.findall(r"[a-zA-Z]+", text))

# [0-9] - digits (same as \d)
print(re.findall(r"[0-9]+", text))

# [^...] - negation: anything NOT in the set
# [^a-zA-Z] - anything that is not a letter
print(re.findall(r"[^a-zA-Z ]+", text))

# Combining ranges: letters, digits, and specific characters
# Match date-like patterns: digits and /
print(re.findall(r"[0-9/]+", text))

# Match phone-like patterns: digits, + and -
print(re.findall(r"[0-9+\-]+", text))

# Equivalences:
# [0-9]   is the same as \d
# [^0-9]  is the same as \D
# [a-zA-Z0-9_] is the same as \w
# [^a-zA-Z0-9_] is the same as \W