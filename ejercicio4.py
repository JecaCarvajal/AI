numero1 = int((input("ingrese el primer numero  ")))
numero2 = int((input("ingrese el segundo numero  ")))

if(numero1 > numero2):
    print("el numero 1 es mayor")
elif (numero2 > numero1):
    print("el numero 2 es mayor")
else:
    print("son iguales")

par = int((input("ingrese un numero  ")))

if(par%2 == 0):
    print("es par")
else:
    print("no es par")

nota = int((input("ingrese la nota  ")))
if nota >=90:
    print("Exelente")
elif nota >= 70 and nota <= 89 :
    print("Bueno")
elif nota >= 50 and nota <= 69 :
    print("Regular")
else:
    print("Reprobado")

palabra = (input("escribe una palabra "))
volteada = palabra[::-1]

if palabra.lower() == volteada.lower():
    print("Es un polidromo")
else:
    print("no es un polidromo")


    
