""" Dado información del usuario, calcular si índice corporal e imprimir su 
grado de obesidad """

""" estatura = float(input("dame tu estatura: "))
peso= float(input("dame tu peso: "))

if estatura > 1.80 :
    print(f'tu estatura es {estatura}')
else:
    print('Eres bajito jajaja')
if peso > 50:
    print("y delgado")
else:
    print("gordito") """

Estatura = float(input("¿Cuál es tu estatura?"))
Peso = float(input("ahora dame tu peso: ")) 
imc= round(Peso/(Estatura**2),2)
if imc > 0 and imc < 18:
    print(f"Estas delgado come más, tu imc es de : {imc}")
if imc > 18.1 and imc <25:
    print(f"Estas en rango  quédate así, tu imc es de {imc}")
if imc  >25.1 and imc < 30:
    print(f"Estas gordo jajajajaja tu imc es de {imc}")
elif imc > 30.1 :
    print(f"amig@ estas en problemas, cuuuiiidate tu imc es de {imc}")
    