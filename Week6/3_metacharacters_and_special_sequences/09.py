# quantifiers: * + ?
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetitions (optional)

import re

text1 = "ac abc abbc abbbc abbbbbbc"

# * matches 0 or more b's between a and c
print(re.findall(r"ab*c", text1))     # ['ac', 'abc', 'abbc', 'abbbc', 'abbbbbbc']

text2 = "acabcabbcabbbcabbbbbbc"

# will give us the longest match
print(re.match(r"a.*c", text1))

# + matches 1 or more b's between a and c
print(re.findall(r"ab+c", text1))     # ['abc', 'abbc', 'abbbc', 'abbbbbbc']

# ? matches 0 or 1 b between a and c
print(re.findall(r"ab?c", text1))     # ['ac', 'abc']

# Practical example: matching optional "s" for plural
words = "cat cats dog dogs bird"
print(re.findall(r"\b\w+s?\b", words))