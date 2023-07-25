from random import randint

numbers = []
for i in range(13):
    numbers.append(randint(1, 8))

new_list = []
for elem in set(numbers):
    if numbers.count(elem) > 1:
        new_list.append(elem)


print(f'{numbers}')
print(f'{new_list}')