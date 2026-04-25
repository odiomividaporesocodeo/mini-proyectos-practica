import re

def validar_contraseña():
    intentos = 0
    while intentos < 3:
        contraseña = input("Ingrese su contraseña: ")
        errores = []
        if len(contraseña) < 8:
            errores.append("Su contraseña debe contener al menos 8 caracteres")
            
        else:
            if not re.search(r"[A-Z]", contraseña):
                errores.append("Debe contener al menos una mayúscula")
            if not re.search(r"[a-z]", contraseña):
                errores.append("Debe contener al menos una minúscula")
            if not re.search(r"[0-9]", contraseña):
                errores.append("Debe contener al menos un número")

        if errores:
            intentos += 1
            print("\n".join(errores))
            print(f"Intento {intentos}/3 fallido")
        else:
            print("Contraseña Válida")
            return True
    print("Se alcanzó el límite de intentos")
    return False
validar_contraseña()     