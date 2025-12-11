# ---------------------------------------------------------
# PROGRAMA: Promedio semanal del clima
# PARADIGMA: Programación Orientada a Objetos (POO)
# AUTOR: Belgica Jomayra Licto
# ---------------------------------------------------------
# En este paradigma se utilizan clases, objetos, atributos
# y métodos para organizar el programa.
class ClimaSemanal:

    def __init__(self):
        # Atributo: lista de temperaturas
        self.temperaturas = []

    # Método que pide los datos al usuario
    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    # Método que calcula el promedio semanal
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método que organiza todo el proceso
    def ejecutar(self):
        print("=== PROGRAMACIÓN POO ===")
        self.ingresar_temperaturas()
        promedio = self.calcular_promedio()
        print(f"El promedio semanal es: {promedio:.2f} °C")

# Crear objeto y ejecutar programa
programa = ClimaSemanal()
programa.ejecutar()