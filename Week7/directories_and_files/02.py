import os

path = r'C:\Users\chris\OneDrive\Документы\Test_repo_2026\Week7\directories_and_files' # absolute path
# .. - shorthand for previous directory
# .  - shorthand for current directory

contents = os.listdir(path)

for element in contents:
    print(element)