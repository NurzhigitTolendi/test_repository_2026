import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = 'john' # our regex

result = re.match(pattern, text_to_match) # return None - no match
# becuase match() requires the match to happen at the beginning of the string
# use search() instead for such cases

print(result) # None

print(result.group()) # error, not a match object