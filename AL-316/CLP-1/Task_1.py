numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")

