my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = []
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break
    numbers.append(my_list[index])
    index = index + 1
numbers.remove(0)
print(numbers)