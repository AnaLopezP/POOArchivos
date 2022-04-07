import csv
lista = []
#estructura general:
def calif_to_lista():
    with open ('calificaciones.csv') as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimitador)
        sort = sorted(leer, key = 'Apellidos')
        for i in sort:
            lista.append(i)
        return lista



def añadir_final():
    pass
def aprobados_suspensos():
    pass

print(calif_to_lista())