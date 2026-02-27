import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = 'john' # our regex

result = re.search(pattern, text_to_match)

print(result) # match object

print(result.group()) # print the match as a string