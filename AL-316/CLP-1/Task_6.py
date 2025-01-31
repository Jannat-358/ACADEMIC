n = int(input('Enter the number: '))
first = 0
second = 1

print('Series:', end=' ')

print(first, end=' ')
print(second, end=' ')

for i in range(3, n + 1):
    next_num = first + second
    print(next_num, end=' ')
    first = second
    second = next_num

