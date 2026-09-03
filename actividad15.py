import struct

ARCHIVO = "datos.bin"

def registrar_videojuego():
    try:
        id = int(input("Ingrese el ID del videojuego: "))
        titulo = input("Ingrese el título del videojuego: ")
        plataforma = input("Ingrese la plataforma (ej. PC, PS, XB): ")
        precio = float(input("Ingrese el precio: "))
        desarrollador = input("Ingrese el desarrollador: ")
        editor = input("Ingrese el editor: ")
        fecha_lanzamiento = input("Ingrese la fecha de lanzamiento (8 caracteres, ej. DD/MM/YY o DD-MM-YY): ")
        clasificacion_edad = input("Ingrese la clasificación de edad (3 caracteres, ej. +10, 12+, +18): ")
        descripcion = input("Ingrese la descripción del videojuego: ")

        titulo_bytes = titulo.encode("utf-8")
        desarrollador_bytes = desarrollador.encode("utf-8")
        editor_bytes = editor.encode("utf-8")
        descripcion_bytes = descripcion.encode("utf-8")

        longitud_titulo = len(titulo_bytes)
        longitud_desarrollador = len(desarrollador_bytes)
        longitud_editor = len(editor_bytes)
        longitud_descripcion = len(descripcion_bytes)

        with open(ARCHIVO, "ab") as archivo:
            archivo.write(struct.pack("<i", id))

            archivo.write(struct.pack("<I", longitud_titulo))
            archivo.write(titulo_bytes)

            archivo.write(struct.pack("2s", plataforma.encode("utf-8")))

            archivo.write(struct.pack("<f", precio))

            archivo.write(struct.pack("<I", longitud_desarrollador))
            archivo.write(desarrollador_bytes)

            archivo.write(struct.pack("<I", longitud_editor))
            archivo.write(editor_bytes)

            archivo.write(struct.pack("8s", fecha_lanzamiento.encode("utf-8")))

            archivo.write(struct.pack("3s", clasificacion_edad.encode("utf-8")))

            archivo.write(struct.pack("<I", longitud_descripcion))
            archivo.write(descripcion_bytes)

        print("\nVideojuego registrado exitosamente.\n")

    except ValueError:
        print("\nError: Asegúrese de ingresar valores válidos.\n")
        return


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