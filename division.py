def dividir():
    
    print("*" * 50)
    print("Se encuentra en la seccion de division")
    print("*" * 50)
    print("\nPara salir de la division, escriba 'fin'")
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
    try:
        resultado = lista[0]
        for num in lista[1:]:
            if num == 0:
                raise ZeroDivisionError
            resultado /= num
        print("La division es: ", resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    opcion=input("Desea volver a dividir? (s/n): ")
    if opcion == "s":
        dividir()