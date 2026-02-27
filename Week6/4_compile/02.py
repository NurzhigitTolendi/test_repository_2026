# compile() - why use it?
# When you reuse the same pattern multiple times, compiling it once is cleaner and faster.
# Without compile, Python re-parses the pattern string on every call.

import re

emails = [
    "john.doe@example.com",
    "not-an-email",
    "alice_99@work.net",
    "bad@",
    "bob.smith@company.org",
]

# Compile the pattern once
email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$')

# Reuse it across multiple calls
for entry in emails:
    if email_pattern.match(entry):
        print(f"  Valid:   {entry}")
    else:
        print(f"  Invalid: {entry}")