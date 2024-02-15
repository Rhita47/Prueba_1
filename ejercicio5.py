
import random

# Generate a random 16-digit number
random_number = str(random.randint(10**15, (10**16)-1))

# Divide the number into 4 equal parts
part_length = len(random_number) // 4
parts = [random_number[i:i+part_length] for i in range(0, len(random_number), part_length)]

# Print each part on a separate line
for part in parts:
    print(part)     