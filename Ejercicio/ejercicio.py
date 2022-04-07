import csv
import operator
info_alumnos = []
#estructura general:
#funcion que ordena por apellidos en orden alfabetico
def calif_to_lista():
    with open ('calificaciones.csv', encoding = 'UTF-8') as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimiter = delimitador)
        for row in leer:
            info_alumnos.append(row)
        sort = sorted(info_alumnos, key = operator.itemgetter('Apellidos'))
        for row in sort:
            print(row['Apellidos'], row['Nombre'])
    return info_alumnos



def añadir_final():
    pass
def aprobados_suspensos():
    pass

calif_to_lista()