from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo= "grupo predeterminado", asignaturas = None, estudiantes = None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas = {}
        for key in kwargs:
            self._asignaturas[key] = kwargs[key]

    def agregarAlumno(self, alumno, lista = None):
        if (lista is None):
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f'Grupo de estudiantes: {self._grupo}'
