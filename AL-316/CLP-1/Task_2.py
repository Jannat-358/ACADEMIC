numbers = {23, 45, 12, 89, 5, 38}

smallest = float('inf')

for num in numbers:
    if num < smallest:
        smallest = num

print(f"Smallest number: {smallest}")
