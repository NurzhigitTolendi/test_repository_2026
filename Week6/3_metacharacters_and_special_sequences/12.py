# special sequences: \s \S \b \B

import re

text = "John's email is john.doe@example.com, and his phone is +7-555-123-4567."

# \s - any whitespace character (space, tab, newline)
print(re.findall(r"\s+", text))

# \S - any non-whitespace character
print(re.findall(r"\S+", text))

# \b - word boundary (between a \w and a \W character)
# Useful for matching whole words only
print(re.findall(r"john", text))     # ['john'] - only lowercase
print(re.findall(r"\bjohn\b", text)) # ['john'] - whole word "john" only

# Without \b, "his" would also match inside other words:
print(re.findall(r"his", text))      # ['his', 'his'] - matches "his" in both places
print(re.findall(r"\bhis\b", text))  # ['his', 'his'] - both are standalone here

# \B - NOT a word boundary (inside a word)
print(re.findall(r"\Bohn", text))    # ['ohn', 'ohn'] - "ohn" only when NOT at start of word