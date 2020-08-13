""" number = input('Dame un número: ')
print(number)
print(type(number))
number = int(number)
print(number)
print(type(number))
for i in range(10):
    index = i + 1
    text = f'{number} * {index} = {index*number}'
    print(text)7 """

numero = int(input('Dame un número: '))
for i in range(10):
    print(f'{numero} * {i + 1} = {(i + 1)*numero}')