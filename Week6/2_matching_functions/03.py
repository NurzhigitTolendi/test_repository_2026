import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = '[Jj]ohn' # our regex

result = re.findall(pattern, text_to_match)

print(result) # list of strings