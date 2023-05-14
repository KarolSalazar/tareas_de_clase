def solicitar_edad():
    edad = int(input("Por favor, ingrese su edad (en números): "))
    return edad

def solicitar_mes():
    mes = int(input("Por favor, ingrese su mes de nacimiento (en números): "))
    return mes

def definir_edad():
    edad = solicitar_edad()
    if edad >= 0:
        mes = solicitar_mes()
        if mes <= 12 and mes > 0:
            if edad >= 18:
                print("Es mayor de edad")
            else:
                print("Es menor de edad")
        else:
            print("¿Qué clase de calendario es ese?")
    else:
        print("RESPETE")

definir_edad()