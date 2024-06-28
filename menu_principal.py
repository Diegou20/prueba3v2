import json
from mantenedor_usuarios import mantenedor_usuarios

def cargar_datos():
    try:
        with open('biblioteca.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"Autor": [], "Categoria": [], "Libro": [], "Usuario": [], "Prestamo": []}

def mostrar_menu_principal():
    print("****************************************")
    print("*              MUNDO LIBRO             *")
    print("****************************************")
    print("[1] - Mantenedor de usuarios")
    print("[2] - Reportes")
    print("[3] - Salir")

def main():
    datos = cargar_datos()
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mantenedor_usuarios(datos)
        elif opcion == "2":
            print("Funcionalidad de reportes no implementada.")
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()

