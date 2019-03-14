bucle1 = 1
lista = []
def adicionar():
    numero = int(input("digite el numero que desea agregar a la lista"))
    lista.append(numero)

def adicionar_al_final():
    numero = int(input("digite el numero que desea agregar a la lista"))
    lista.append(numero)

def adicionar_segun_posicion():
    posicion = int(input("digite la posicion en cual desea agregar el numero a la tabla"))
    numero = int(input("digite el numero que agregara a la tabla"))
    lista.insert(posicion, numero)

def consultar_dato():
    n = len(lista)
    print("tenga en cuentaque la lista tiene ",n,"datos")
    numero = int(input("digite el numero que desea saber la posicion"))
    print (lista.index(numero))
def eliminar_dato():
    numero = int(input("digite el numero que desea eliminar"))
    print("se ha remoivo el numero ",numero)
    lista.remove(numero)
def invertir():
    lista.reverse
    print(lista)
while bucle1 == 1:
   try:
        adicionar()
        bucle1 = int(input("1.agregar"+"\n"+"2.adicionar al final"+"\n"+"3.adicionar segun posicion"+"\n"+"4.consultar"+"\n"+"5.eliminar"+"\n"+"6.invertir"))
        if bucle1 == 2:
            adicionar_al_final()
        if bucle1 == 3:
            adicionar_segun_posicion()
        if bucle1 == 4:
            consultar_dato()
        if bucle1 == 5:
            eliminar_dato()
        if bucle1 == 6:
            invertir()
        bucle1 = int(input("1 para repetir" ))
   except:
        print("verifique sus datos")
    

    