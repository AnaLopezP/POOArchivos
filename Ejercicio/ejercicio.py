import csv

#estructura general:
def calif_to_lista():
    with open ('calificaciones.csv') as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimitador)
        for i in leer:
            print(i)



def añadir_final():
    pass
def aprobados_suspensos():
    pass

print(calif_to_lista())