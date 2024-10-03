#LISTAS
#Lista de Nombres
nombres = ["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]
#Harry Houdini, David Blaine y Teller son magos
magos = ["Harry Houdini","David Blaine","Teller"]
#Newton, Hawking y Einstein son científicos
cientificos = ["Newton","Hawking","Einstein"]
#Otros
otros = []

#Funcion para recorrer las listas
def imprimir_nombres(lista_nombres):
    for nombre in lista_nombres:
        print(nombre)

print("Lista completa de nombres:")
imprimir_nombres(nombres)
print("-------------------")

#Funcion para Magos Grandiosos
def hacer_grandiosos(lista_magos):
    magos_grandiosos = []
    for mago in lista_magos:
        magos_grandiosos.append(f"El gran " + mago)
    return magos_grandiosos

magos_grandiosos = hacer_grandiosos(magos)
print("Magos grandiosos:")
imprimir_nombres(magos_grandiosos)
print("-------------------")

print("Cientificos: ")
imprimir_nombres(cientificos)
print("-------------------")

#Otros
for nombre in nombres:
    if nombre in magos:
        continue
    elif nombre in cientificos:
        continue
    else:
        otros.append(nombre)
print("Otros: ")
imprimir_nombres(otros)
print("-------------------")
