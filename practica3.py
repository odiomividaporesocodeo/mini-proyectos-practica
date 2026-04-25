def tablas():
    while True:
        try:
            numero = int(input("Ingrese el número que desea multiplicar: "))
            if 10 >= numero > 0:
                for i in range(1, 10 + 1):
                    print(f"{numero} * {i} es: {numero * i}")
                break
            else:
                print("Ingrese un número del 1 al 10")
        except ValueError:
            print("Ingrese un valor válido")
tablas()

def pares():
    while True:
        try:
            inicio = int(input("Ingrese el inicio: "))
            fin = int(input("Ingrese el fin: "))
            numeros_pares = []
            if fin > inicio:
                for i in range(inicio, fin + 1):
                    if i % 2 == 0:
                        numeros_pares.append(i)
                print(f"Los números pares fueron: {", ".join(str(n) for n in numeros_pares)}")
                break
            else:
                print("Fin debe ser mayor a Inicio")
        except ValueError:
            print("No puede ingresar otra cosa que no sean números")

pares()

def notas_alumnos():
    try:
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        if cantidad_alumnos > 0:
            suma_notas = 0
            for i in range(1, cantidad_alumnos + 1):
                while True:
                    try:
                        nota = int(input("Ingrese la nota del alumno: "))
                        if 1 <= nota <= 10:
                            suma_notas += nota
                            break
                        else:
                            print("La nota debe ser del 1 al 10")
                    except ValueError:
                        print("Ingrese un número entero del 1 al 10")
            print(f"El promedio de las notas es {suma_notas / cantidad_alumnos}")
        else:
            print("No puede tener menos de 0 alumnos")
    except ValueError:
        print("Ingrese un valor válido")

notas_alumnos()

def usuario_par():
    try:
        numeros_pares = []
        par = 0
        for i in range(10):
            pedir_numero = int(input("Ingrese un número: "))
            if pedir_numero % 2 == 0:
                numeros_pares.append(pedir_numero)
                par += 1
        print(f"La cantidad de números pares fueron: {par} y los números fueron: {", ".join(str(n) for n in numeros_pares)}")
    except ValueError:
        print("Ingrese un valor válido")
        return

usuario_par()

def numeros_naturales():
    while True:
        try:
            ingresar_numero = int(input("Ingrese un número: "))
            if ingresar_numero > 0:
                print(f"La suma de los {ingresar_numero} primeros números naturales es: {ingresar_numero * (ingresar_numero + 1) // 2}")
                break
            else:
                print("Debe ingresar un número mayor a 0")
        except ValueError:
            print("Ingrese un valor válido")

numeros_naturales()
    
def factorial():
    while True:
        try:
            ingresar_factorial = int(input("Ingrese el número que desee conseguir su factorial: "))
            resultado = 1
            if ingresar_factorial > 0:
                for i in range(1, ingresar_factorial + 1):
                    resultado *= i
                print(f"El factorial de {ingresar_factorial} es: {resultado}")
                break
            else:
                print("Ingresa un número válido")
        except ValueError:
            print("Ingrese un valor válido")
factorial()