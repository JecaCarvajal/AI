libro  = {
    "titulo":"La vida feliz",
    "autor":"Jeca",
    "año": 2019,
}

libro["Editorial"] = "Carvajal"

print (libro)

empleado  = {
    "nombre":"Carlos",
    "puesto":"Analista",
}

empleado["salario"] = 500000

print(empleado)

coche  = {
    "marca":"Toyota",
    "modelo":"Corrolla",
}

del coche["modelo"]

print(coche)

ciudad  = {
    "nombre":"Londres",
    "poblacion":8900000,
}

print (ciudad["nombre"])

estudiante  = {
    "nombre":"Eduardo",
    "edad":36,
    "isStudent": False,
    "cursos":["Python", "C#"]
}


print(f"El nombre del estidiante es: {estudiante["nombre"]}")
print(f"La edad es : {estudiante["edad"]}")
print(f"Es estudiante : {estudiante["isStudent"]}")
print(f"Los cursos son  : {estudiante["cursos"]}")

for clave, valor in estudiante.items():
  print(f" {clave} del estudiante, {valor}")



