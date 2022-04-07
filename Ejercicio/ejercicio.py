import csv
import operator
info_alumnos = []
#estructura general:
def calif_to_lista():
    with open ('calificaciones.csv', encoding = 'UTF-8') as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimiter = delimitador)
        for row in leer:
            print(row['Apellidos'], row['Nombre'])
        sort = sorted(leer, key = operator.attrgetter('Apellidos'))
        print(sort) 
        for i in sort:
            info_alumnos.append(i)
        print(info_alumnos)
    return info_alumnos



def añadir_final():
    pass
def aprobados_suspensos():
    pass

print(calif_to_lista())