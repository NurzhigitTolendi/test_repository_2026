# random

# https://docs.python.org/3/library/random.html

import random

# Random float between 0.0 and 1.0
print(random.random())

# Random integer in a range (inclusive on both ends)
print(random.randint(1, 100))

# Random float in a range
print(random.uniform(1.0, 10.0))

# Pick a random element from a sequence
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(random.choice(fruits))

# Pick multiple unique elements
print(random.sample(fruits, 3))

# Shuffle a list in-place
random.shuffle(fruits)
print(fruits)

# Reproducible results with a seed
random.seed(42)
print(random.randint(1, 100))  # always the same number with seed 42
print(random.randint(1, 100))  # always the same number with seed 42