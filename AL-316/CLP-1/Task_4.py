numbers = {23, 45, 12, 89, 5, 38}


numbers_list = list(numbers)
n = len(numbers_list)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers_list[j] > numbers_list[j+1]:

            numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]

second_highest = numbers_list[-3]

print(f"Second highest number: {second_highest}")

