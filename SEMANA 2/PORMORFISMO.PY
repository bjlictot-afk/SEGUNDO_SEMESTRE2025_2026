# ---------------------------------------------------------
# EJEMPLO DE POLIMORFISMO EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------

# El polimorfismo permite que diferentes clases
# tengan un método con el MISMO nombre,
# pero que cada una lo implemente de manera distinta.

class Animal:

    # Método que será "polimórfico"
    def hacer_sonido(self):
        pass


# ---------------------------------------------------------
# CLASE HIJA 1
# ---------------------------------------------------------
class Perro(Animal):

    def hacer_sonido(self):
        return "Guau"


# ---------------------------------------------------------
# CLASE HIJA 2
# ---------------------------------------------------------
class Gato(Animal):

    def hacer_sonido(self):
        return "Miau"