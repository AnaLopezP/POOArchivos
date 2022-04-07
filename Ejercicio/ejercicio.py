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



def añadir_final(lista):
    for i in lista:
        nota_parcial1 = i.get('Parcial1')
        nota_parcial2 = i.get('Parcial2')
        nota_practicas = i.get('Practicas')
        i['Final'] = float(nota_parcial1)*0.3 + float(nota_parcial2)*0.3 + float(nota_practicas)*0.4






def aprobados_suspensos():
    pass

calif_to_lista()
añadir_final(info_alumnos)