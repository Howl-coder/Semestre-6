def tamanos(L):
    L=L[1:]
    x=len(L)
    if x<1 or x>5:
        print( "Un maximo de 5 tamaños minimo 1")
        insertar()
    for i in range(1,len(L)):
        if i<1 or i>48:
            print("Tamaño fuera de rango")
            insertar()
    if sorted(L) != L:
        print ("Tamaños no estan de forma ascendente")
        insertar()
    for i in range(0, len(L)):
        d = L[i].strip()
        if d.replace('.', '', 1).isdigit() and not float(d).is_integer():
            print( "Contiene decimales")
            insertar()
    print("Se ha insertado correctamente")

def soda(L,bebida):
    x=len(bebida)
    if any(char.isdigit() for char in bebida):
        print("No usar digitos en la bebida")
        insertar()
    if x<2 or x>15:
        print("No puede ser menor a a 2 chars o a mayor a 15 chars")
        insertar()
    tamanos(L)

def insertar():
    valores=input()
    valores=valores.replace(" ", "")
    lis = valores.split(",")
    bebida = lis[0]
    soda(lis,bebida)

insertar()