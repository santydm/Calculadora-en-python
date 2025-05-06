
def suma():
    print("*" * 50)
    print("Se encuentra en la seccion de suma")
    print("*" * 50)
    print("\nPara salir de la suma, escriba 'fin'")
    lista = []
    while True:
        numeros=input("ingrese: ")   
        if numeros.lower() == "fin":
            break
        if numeros == "":
            print("No se ha ingresado nada")
            continue
        try:
            float(numeros)
        except ValueError:
            print("No es un numero")
            continue
        lista.append(float(numeros))
        resultado=sum(lista)   
    print("La suma es: ", resultado)
    opcion=input("Desea vovler a sumar? (s/n): ")
    if opcion == "s":
        suma()

