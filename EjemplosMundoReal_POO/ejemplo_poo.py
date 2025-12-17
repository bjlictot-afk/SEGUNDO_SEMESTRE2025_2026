# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")


# Clase que representa un curso
class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes del curso {self.nombre_curso}:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()


# Creación de objetos
est1 = Estudiante("Ana", "Ingeniería")
est2 = Estudiante("Carlos", "Sistemas")

curso = Curso("Programación I")
curso.agregar_estudiante(est1)
curso.agregar_estudiante(est2)

curso.mostrar_estudiantes()
