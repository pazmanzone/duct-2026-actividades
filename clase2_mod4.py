nombre = "Juan"
apellido = "Perez"
completo = nombre + " " + apellido     # Concatenacion: "Juan Perez"
repetido = "ha" * 3                    # Repeticion: "hahaha"
longitud = len(completo)               # Largo: 10
mayusculas = completo.upper()          # "JUAN PEREZ"
minúsculas = completo.lower()          # "juan perez"
reemplazo = completo.replace("Juan", "Carlos")  # "Carlos Perez"
contain = "Juan" in completo           # True
partes = completo.split(" ")           # ["Juan", "Perez"]
unido = " - ".join(partes)             # "Juan - Perez"

print("Nombre completo:", completo)")
