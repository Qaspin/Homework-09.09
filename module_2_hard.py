a = int(input('Введите число от 3 до 20: '))
name = ''
for i in range(1,a):
    for j in range(i + 1, a):
         if a % (i + j) == 0:
            name += str(i) + str(j)
print(name)
