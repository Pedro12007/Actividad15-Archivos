import struct

ARCHIVO = "datos.bin"

def registrar_videojuego():
    pass

def mostrar_videojuegos():
    pass

def buscar_videojuego():
    pass

def mostrar_posiciones():
    pass

def mostrar_tamanos():
    pass

def mostrar_tamano_total():
    pass



def menu():
    while True:
        print("----- MENU -----")
        print("1. Registrar videojuego.")
        print("2. Mostrar todos los videojuegos registrados.")
        print("3. Buscar un videojuego por su id.")
        print("4. Mostrar la posición inicial de cada registro.")
        print("5. Mostrar cuantos bytes ocupa cada registro.")
        print("6. Mostrar el tamaño total del archivo.")
        print("7. Salir.\n")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1": 
                registrar_videojuego()
            case "2":
                mostrar_videojuegos()
            case "3":
                buscar_videojuego()
            case "4":
                mostrar_posiciones()
            case "5":
                mostrar_tamanos()
            case "6":
                mostrar_tamano_total()
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")


if __name__ == "__main__":
    menu()