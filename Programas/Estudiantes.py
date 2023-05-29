# Dirección Actual
# Nombre
# Carné
# Promedio

class Estudiante:

    # Constructor
    def __init__(self, nombre_completo, carne, direccion):
        self.direccion_actual = direccion
        self.nombre, self.apellido = nombre_completo.split()
        self.carne = carne
        self.promedio = 0.0

    # Comportamientos
    # Notas es una lista de parejas (x, y)
    # donde x es el nombre de la materia y Y es la nota final
    def calcular_promedio(self, notas):
        prom = 0.0
        for nota in notas:
            prom += nota[1]
        self.promedio = prom / len(notas)

    def __str__(self):
        return str({
            'Nombre': self.nombre,
            'Apellido': self.apellido,
            'Carné': self.carne,
            'Promedio': self.promedio
        })


def main():
    e1 = Estudiante('Angie Mojica', '123456789', 'Av Rosa # 57 - 22 sector 2')
    e2 = Estudiante('Juan Daza', '0456789', 'Av Springfield # 44 - 67')
    estudiantes = [e1, e2]
    e1.calcular_promedio([('AYED', 3.5), ('MMIN', 4.2), ('CALD', 2.5)])
    for e in estudiantes:
        print(e)


main()
