import csv

#estructura general:
def calif_to_lista():
    open ('calificaciones.csv')
    file = 'calificaciones.csv'
    delimitador = ';'
    leer = csv.DictReader(file, delimitador)
    for i in leer:
        print(i)



def añadir_final():
    pass
def aprobados_suspensos():
    pass

print(calif_to_lista())