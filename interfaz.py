from sumar import suma
from restar import resta

def menu():
    while True:
        print("*" * 50)
        print("Bienvenido a la calculadora en Python")
        print("*" * 50)
        print("Escoge entre las siguientes opciones: \n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("*" * 50)

        opcion = input("Ingrese el numero de la opcion que desea utilizar: ")

        if opcion == "1":
            print("Has elegido la suma")
            suma()
        elif opcion == "2":
            resta()
            print("Has elegido la resta")
        elif opcion == "3":
            print("Has elegido la multiplicacion")
        elif opcion == "4":
            print("Has elegido la division")
        elif opcion.lower() == "s":
            print("Saliendo de la calculadora...")
            break
        

menu()