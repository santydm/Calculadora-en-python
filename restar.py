def resta():
    print("*" * 50)
    print("Se encuentra en la seccion de resta")
    print("*" * 50)
    print("\nPara salir de la resta, escriba 'fin'")
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
        resultado=lista[0]
        for num in lista[1: ]:
            resultado -= num
    print("La resta es: ", resultado)
    opcion=input("Desea volver a restar? (s/n): ")
    if opcion == "s":
        resta()