nombre = "Eneko"
apellido = "Isasi"
edad = 54
direccion = "Ramon Rubial, 15"
print(nombre)
print(f"Hola, mi nombre es {nombre} {apellido} y vivo en {direccion}")
print("Comprobación de sincronización realizada con éxito.")
# Variables numéricas y booleanas
altura = 1.80          # Esto es un Float
estudiante = True      # Esto es un Boolean (Nota la mayúscula)

# Operaciones con variables
puntuacion_total = 10 + 5
es_mayor_de_edad = edad >= 18  # Comparación que devuelve un Boolean

print(f"¿Es {nombre} mayor de edad?: {es_mayor_de_edad}")
print(f"Su altura es de {altura} metros.")
altura = altura + 0.05
print(f"Si me pongo zapatos, mido {altura} metros.")
# --- Ejercicio 1: Intercambio de variables ---
vaso_rojo = "Agua"
vaso_azul = "Vino"

print(f"Antes: Rojo tiene {vaso_rojo} y Azul tiene {vaso_azul}")

# Tu reto: Intercambia los contenidos. 
# Pista: Usa una variable llamada 'ayuda' para no derramar nada.

ayuda = vaso_rojo
vaso_rojo = vaso_azul
vaso_azul = ayuda

print(f"Después: Rojo tiene {vaso_rojo} y Azul tiene {vaso_azul}")
print("Ejercicio 1 completado con éxito!")
print("Ejercicio 2 completado con éxito!")  
precio = 100
iva = precio * 0.21
total = precio + iva
print(f"El total con IVA es: {total}")
