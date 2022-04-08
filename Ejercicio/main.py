import ejercicio

if __name__ =='__main__':
    info_alumnos = []

    info_alumnos = ejercicio.calif_to_lista()
    ejercicio.añadir_final(info_alumnos)
    aprobados,suspensos = ejercicio.aprobados_suspensos(info_alumnos)
    print("----------------APROBADOS--------------------------")
    print(aprobados)
    print("----------------SUSPENSOS--------------------------")
    print(suspensos)
        