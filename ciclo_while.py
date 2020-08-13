""" amigos = []
while len(amigos) < 5:
    nombre = input('Nombra un amigo: ')
    amigos.append(nombre)
lista_nombres = ', '.join(amigos)
print(f'Listado de amigos\n{lista_nombres}') """

obesidad = []
while len(obesidad) < 4:
    estatura = input("dame tu estatura: ")
    obesidad.append(estatura)
    lista_estatura = ','.join(obesidad)
    
print(f"tu peso es {estatura}\n{lista_estatura}")
