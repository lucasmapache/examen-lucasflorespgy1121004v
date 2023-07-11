
deptos = []
compra = []
ganancias = []

tipo_A = 3800
tipo_B = 3000
tipo_C = 2800
tipo_D = 3500

def pisos_depto():
    global deptos
    for i in range(10):
        deptos.append( [f"A{i+1}", f"B{i+1}", f"C{i+1}", f"D{i+1}"])

def deptos_disp():
    for i in range(10):
        print(f"Piso {i+1}: {deptos[i]}")

def compra_depto():
    global deptos, ganancias, compra
    piso = int(input("Ingrese el número de piso (1-10) :"))
    tipo = input("Ingrese el tipo de departamento que desea (A, B, C, D) :").upper()
    rut=int(input("Ingrese su rut :"))
    if piso < 1 or piso > 10:
        print("Número de piso inválido")
        return
    if tipo not in ["A", "B", "C", "D"]:
        print("Tipo de departamento inválido")
        return
    depto = f"{tipo}{piso}"
    if depto not in deptos[piso-1]:
        print("Departamento no disponible")
        return
    deptos[piso-1].remove(depto)
    compra.append(depto)
    if tipo == "A":
        ganancias.append(tipo_A)
    elif tipo == "B":
        ganancias.append(tipo_B)
    elif tipo == "C":
        ganancias.append(tipo_C)
    elif tipo == "D":
        ganancias.append(tipo_D)
    print("Departamento comprado")

def lista_deptos():
    global deptos
    for i in range(len(deptos)):
        print(f"Piso {i+1}: {deptos[i]}")

def ganancias_totales():
    total_ganancias =+(ganancias)
    print(f"Las ganancias totales fueron: {ganancias}")

def ejecucion_programa():
    while True:
        print("\t\t Bienvenido a la inmobiliaria \"CASA FELIZ\"")
        print("1- Comprar departamento")
        print("2-Mostrar departamentos disponibles")
        print("3- Ver listado de compradores")
        print("4-Mostrar ganancias totales")
        print("5- Salir")
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            compra_depto()
        elif opc == 2:
            deptos_disp()
        elif opc == 3:
            print(compra)
        elif opc == 4:
            ganancias_totales()
        elif opc == 5:
            print("Hasta luego")
            break
        else:
            print("Ingrese una opción válida")

pisos_depto()
ejecucion_programa()
