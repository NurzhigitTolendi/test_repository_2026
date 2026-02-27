# quantifiers: {n} {n,m} and greedy vs lazy

import re

text = "a1 ab12 abc123 abcd1234 abcde12345"

# {n} - exactly n repetitions
print(re.findall(r"\d{3}", text))       # ['123', '123', '123']

# {n,m} - between n and m repetitions
print(re.findall(r"\d{2,4}", text))     # ['12', '123', '1234', '1234']

# {n,} - n or more repetitions
print(re.findall(r"\d{3,}", text))      # ['123', '1234', '12345']

# Greedy vs Lazy
# By default, quantifiers are greedy - they match as much as possible.
# Adding ? after a quantifier makes it lazy - it matches as little as possible.

html = "<b>bold</b> and <i>italic</i>"

# Greedy: .+ grabs as much as it can
print(re.findall(r"<.+>", html))        # ['<b>bold</b> and <i>italic</i>']

# Lazy: .+? grabs as little as possible
print(re.findall(r"<.+?>", html))       # ['<b>', '</b>', '<i>', '</i>']