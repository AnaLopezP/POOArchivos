import csv
import operator
info_alumnos = []
#estructura general:
def calif_to_lista():
    with open ('calificaciones.csv', encoding = 'UTF-8') as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimitador)
        sort = sorted(leer, key = operator.itemgetter('Apellidos'))
        for i in sort:
            info_alumnos.append(i)
    return info_alumnos



def añadir_final():
    pass
def aprobados_suspensos():
    pass

print(calif_to_lista())