estudiantes = {
    "nombre":"Eduardo",
    "edad":36,
    "IsStudent": True,
    "Nota": 10,
    "Cursos": ["Java", "Python", "C#"]
}

estudiantes["Genero"] = "Masculino"

del estudiantes["IsStudent"]

print (estudiantes)
print (estudiantes["Cursos"])

for clave, valor in estudiantes.items():
  print(f"{clave}, {valor}")