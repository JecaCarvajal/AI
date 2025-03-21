def area_circulo(radio):
    pi = 3.14           
    return pi * (radio**2)

print(area_circulo(5))

def numeros_primos():
    for i in range(1,11):
        if(i%2 == 0):
            print(i)
numeros_primos()

def suma_numeros():
    contador = 1
    suma = 1
    while contador < 100:
        contador = contador + 1
        suma = contador + suma
    print(suma)

suma_numeros()

def encontrar_palabra():
    palabras = ["manzana", "banana", "cereza", "durazno"]
    for p in palabras:
        if(p[0] == "b"):
            print(f"palabra encontrada es {p}")
            break

encontrar_palabra()

