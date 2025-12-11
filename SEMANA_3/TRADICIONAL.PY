# ---------------------------------------------------------
# PROGRAMA: Promedio semanal del clima
# PARADIGMA: Programación Tradicional (Estructurada)
# AUTOR: Belgica Jomayra Licto
# ---------------------------------------------------------
# En este paradigma se utilizan funciones independientes,
# sin crear clases ni objetos.
# Función que pide al usuario las temperaturas de los 7 días
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función que calcula el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal del programa
def main():
    print("=== PROGRAMACIÓN TRADICIONAL ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal es: {promedio:.2f} °C")

# Ejecutar programa
main()