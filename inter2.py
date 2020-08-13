'''
Interpolación con format
Formateo de strings/cadenas
'''
person = 'Galileo'
age = 31
text = '¿Puedes creer que {} tiene {} de edad?'.format(person, age)
print(text)
text = '¿Puedes creer que {user} tiene {number} de edad?'.format(user=person, number=age)
print(text)

person= "Carlos"
age= 22
text='¿puedes creer que {} tiene {}?'.format(person, age )
print(text)