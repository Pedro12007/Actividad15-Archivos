import struct
import os

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


def leer_videojuego(archivo):
    datos_id = archivo.read(4)
    if not datos_id or len(datos_id) != 4:
        return None
    id = struct.unpack("<i", datos_id)[0]

    datos_longitud_titulo = archivo.read(4)
    if len(datos_longitud_titulo) != 4:
        return None
    longitud_titulo = struct.unpack("<I", datos_longitud_titulo)[0]
    titulo_bytes = archivo.read(longitud_titulo)
    if len(titulo_bytes) != longitud_titulo:
        return None
    titulo = titulo_bytes.decode("utf-8")

    datos_plataforma = archivo.read(2)
    if len(datos_plataforma) != 2:
        return None
    plataforma = struct.unpack("2s", datos_plataforma)[0].decode("utf-8").rstrip("\x00")

    datos_precio = archivo.read(4)
    if len(datos_precio) != 4:
        return None
    precio = struct.unpack("<f", datos_precio)[0]

    datos_longitud_desarrollador = archivo.read(4)
    if len(datos_longitud_desarrollador) != 4:
        return None
    longitud_desarrollador = struct.unpack("<I", datos_longitud_desarrollador)[0]
    desarrollador_bytes = archivo.read(longitud_desarrollador)
    if len(desarrollador_bytes) != longitud_desarrollador:
        return None
    desarrollador = desarrollador_bytes.decode("utf-8")

    datos_longitud_editor = archivo.read(4)
    if len(datos_longitud_editor) != 4:
        return None
    longitud_editor = struct.unpack("<I", datos_longitud_editor)[0]
    editor_bytes = archivo.read(longitud_editor)
    if len(editor_bytes) != longitud_editor:
        return None
    editor = editor_bytes.decode("utf-8")

    datos_fecha = archivo.read(8)
    if len(datos_fecha) != 8:
        return None
    fecha_lanzamiento = struct.unpack("8s", datos_fecha)[0].decode("utf-8").rstrip("\x00")

    datos_clasificacion = archivo.read(3)
    if len(datos_clasificacion) != 3:
        return None
    clasificacion_edad = struct.unpack("3s", datos_clasificacion)[0].decode("utf-8").rstrip("\x00")

    datos_longitud_descripcion = archivo.read(4)
    if len(datos_longitud_descripcion) != 4:
        return None
    longitud_descripcion = struct.unpack("<I", datos_longitud_descripcion)[0]
    descripcion_bytes = archivo.read(longitud_descripcion)
    if len(descripcion_bytes) != longitud_descripcion:
        return None
    descripcion = descripcion_bytes.decode("utf-8")

    return id, titulo, plataforma, precio, desarrollador, editor, fecha_lanzamiento, clasificacion_edad, descripcion


def mostrar_videojuegos():
    print("\n--- Lista de Videojuegos Registrados ---")
    try:
        with open(ARCHIVO, "rb") as archivo:
            numero_registro = 1
            while True:
                posicion_inicial = archivo.tell()
                videojuego = leer_videojuego(archivo)

                if videojuego is None:
                    if numero_registro == 1:
                        print("No hay videojuegos registrados en el archivo.")
                    break

                posicion_final = archivo.tell()
                (id, titulo, plataforma, precio, desarrollador,
                 editor, fecha_lanzamiento, clasificacion_edad, descripcion) = videojuego

                tamanio_registro = posicion_final - posicion_inicial

                print(f"\nRegistro #{numero_registro}")
                print(f"Posición inicial: {posicion_inicial}")
                print(f"Posición final: {posicion_final}")
                print(f"Tamaño: {tamanio_registro} bytes")
                print(f"ID: {id}")
                print(f"Título: {titulo}")
                print(f"Plataforma: {plataforma}")
                print(f"Precio: {precio:.2f}")
                print(f"Desarrollador: {desarrollador}")
                print(f"Editor: {editor}")
                print(f"Fecha de lanzamiento: {fecha_lanzamiento}")
                print(f"Clasificación de edad: {clasificacion_edad}")
                print(f"Descripción: {descripcion}")

                numero_registro += 1
            print()
    except FileNotFoundError:
        print("\nEl archivo todavía no existe.\n")

def buscar_videojuego():
    try:
        id_buscado = int(input("Ingrese el ID del videojuego a buscar: "))
    except ValueError:
        print("\nError: El ID debe ser un número entero.\n")
        return

    try:
        with open(ARCHIVO, "rb") as archivo:
            while True:
                posicion = archivo.tell()
                videojuego = leer_videojuego(archivo)

                if videojuego is None:
                    break

                (id, titulo, plataforma, precio, desarrollador,
                 editor, fecha_lanzamiento, clasificacion_edad, descripcion) = videojuego

                if id == id_buscado:
                    print("\n--- Videojuego Encontrado ---")
                    print(f"Posición inicial en archivo: Byte {posicion}")
                    print(f"ID: {id}")
                    print(f"Título: {titulo}")
                    print(f"Plataforma: {plataforma}")
                    print(f"Precio: ${precio:.2f}")
                    print(f"Desarrollador: {desarrollador}")
                    print(f"Editor: {editor}")
                    print(f"Fecha de lanzamiento: {fecha_lanzamiento}")
                    print(f"Clasificación de edad: {clasificacion_edad}")
                    print(f"Descripción: {descripcion}\n")
                    return

        print(f"\nNo se encontró ningún videojuego con el ID {id_buscado}.\n")

    except FileNotFoundError:
        print("\nEl archivo todavía no existe.\n")

def mostrar_posiciones():
    print("\n--- Posición Inicial de Cada Registro ---")
    try:
        with open(ARCHIVO, "rb") as archivo:
            numero_registro = 1
            while True:
                posicion_inicial = archivo.tell()
                videojuego = leer_videojuego(archivo)

                if videojuego is None:
                    if numero_registro == 1:
                        print("No hay videojuegos registrados en el archivo.")
                    break

                id_juego = videojuego[0]
                titulo = videojuego[1]

                print(f"Registro #{numero_registro} | ID: {id_juego} | Título: '{titulo}' -> Posición inicial: Byte {posicion_inicial}")
                numero_registro += 1
            print()
    except FileNotFoundError:
        print("\nEl archivo todavía no existe.\n")

def mostrar_tamanos():
    print("\n--- Tamaño en Bytes de Cada Registro ---")
    try:
        with open(ARCHIVO, "rb") as archivo:
            numero_registro = 1
            while True:
                posicion_inicial = archivo.tell()
                videojuego = leer_videojuego(archivo)

                if videojuego is None:
                    if numero_registro == 1:
                        print("No hay videojuegos registrados en el archivo.")
                    break

                posicion_final = archivo.tell()
                tamanio = posicion_final - posicion_inicial

                id_juego = videojuego[0]
                titulo = videojuego[1]

                print(f"Registro #{numero_registro} | ID: {id_juego} | Título: '{titulo}' | Tamaño: {tamanio} bytes")
                numero_registro += 1
            print()
    except FileNotFoundError:
        print("\nEl archivo todavía no existe.\n")

def mostrar_tamano_total():
    print("\n--- Tamaño Total del Archivo ---")
    try:
        tamano_total = os.path.getsize(ARCHIVO)
        print(f"Tamaño total del archivo: {tamano_total} bytes\n")
    except FileNotFoundError:
        print("\nEl archivo todavía no existe.\n")



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