# special sequences: \d \D \w \W

import re

text = "Order #42: 3 items at $19.99 each (total: $59.97)"

# \d - any digit [0-9]
print(re.findall(r"\d+", text))    # ['42', '3', '19', '99', '59', '97']

# \D - any non-digit [^0-9]
print(re.findall(r"\D+", text))    # ['Order #', ': ', ' items at $', '.', ' each (total: $', '.', ')']

# \w - any word character [a-zA-Z0-9_]
print(re.findall(r"\w+", text))    # ['Order', '42', '3', 'items', 'at', '19', '99', 'each', 'total', '59', '97']

# \W - any non-word character [^a-zA-Z0-9_]
print(re.findall(r"\W+", text))    # [' #', ': ', ' ', ' ', ' $', '.', ' ', ' (', ': $', '.', ')']