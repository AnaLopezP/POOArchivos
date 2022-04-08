import csv
import operator
import locale
info_alumnos = []
aprobados = []
suspensos = []
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
    locale.setlocale(locale.LC_ALL, 'nl_NL')
    for i in lista:
        nota_parcial1 = i.get('Parcial1')
        if not nota_parcial1:
            nota_parcial1= "0"
        nota_parcial2 = i.get('Parcial2')
        if not nota_parcial2:
            nota_parcial2= "0"
        nota_practicas = i.get('Practicas')
        if not nota_practicas:
            nota_practicas = "0"
        
        nota_final = round (locale.atof(nota_parcial1)*0.3 + locale.atof(nota_parcial2)*0.3 + locale.atof(nota_practicas)*0.4, 2)
        i['Final'] = nota_final
    #print(lista)


def aprobados_suspensos(lista):
    locale.setlocale(locale.LC_ALL, 'nl_NL')
    for i in lista:
        nota_parcial1 = i.get('Parcial1')
        if not nota_parcial1:
            nota_parcial1= "0"
        else: 
            nota_parcial1 = locale.atof(nota_parcial1)
        nota_parcial2 = i.get('Parcial2')
        if not nota_parcial2:
            nota_parcial2= 0
        else:
            nota_parcial2 = locale.atof(nota_parcial2)
        nota_final = i.get('Final')
        if not nota_final:
            nota_final = 0
        asistencia = i.get('Asistencia')
        if not asistencia:
            asistencia = 0
        else:
            asistencia = asistencia.removesuffix("%")
            asistencia = locale.atoi(asistencia)
        if asistencia >=75 and nota_parcial1 >=4 and nota_parcial2 >= 4 and nota_final >=5:
            aprobados.append(i)
        else:
            suspensos.append(i)

    return aprobados, suspensos

