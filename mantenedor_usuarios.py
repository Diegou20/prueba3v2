import json

def cargar_datos():
    try:
        with open('biblioteca.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"Autor": [], "Categoria": [], "Libro": [], "Usuario": [], "Prestamo": []}

def guardar_datos(datos):
    with open('biblioteca.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def mostrar_menu_principal():
    print("****************************************")
    print("*              MUNDO LIBRO             *")
    print("****************************************")
    print("[1] - Mantenedor de usuarios")
    print("[2] - Reportes")
    print("[3] - Salir")

def mostrar_menu_mantenedor():
    print("****************************************")
    print("*           MANTENEDOR USUARIO         *")
    print("****************************************")
    print("[1] - Agregar usuario")
    print("[2] - Editar usuario")
    print("[3] - Eliminar usuario")
    print("[4] - Buscar usuario")
    print("[5] - Volver")

def mantenedor_usuarios(datos):
    while True:
        mostrar_menu_mantenedor()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario(datos)
        elif opcion == "2":
            editar_usuario(datos)
        elif opcion == "3":
            eliminar_usuario(datos)
        elif opcion == "4":
            buscar_usuario(datos)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def agregar_usuario(datos):
    usuarios = datos['Usuario']
    nuevo_usuario = {}
    nuevo_usuario['UsuarioID'] = int(input("Ingrese ID del usuario: "))
    nuevo_usuario['Nombre'] = input("Ingrese nombre del usuario: ")
    nuevo_usuario['Email'] = input("Ingrese email del usuario: ")
    nuevo_usuario['FechaRegistro'] = input("Ingrese fecha de registro del usuario: ")
    usuarios.append(nuevo_usuario)
    guardar_datos(datos)
    print("Usuario agregado exitosamente.")

def editar_usuario(datos):
    usuarios = datos['Usuario']
    id_usuario = int(input("Ingrese ID del usuario a editar: "))
    for usuario in usuarios:
        if usuario['UsuarioID'] == id_usuario:
            usuario['Nombre'] = input("Ingrese nuevo nombre del usuario: ")
            usuario['Email'] = input("Ingrese nuevo email del usuario: ")
            usuario['FechaRegistro'] = input("Ingrese nueva fecha de registro del usuario: ")
            guardar_datos(datos)
            print("Usuario editado exitosamente.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(datos):
    usuarios = datos['Usuario']
    id_usuario = int(input("Ingrese ID del usuario a eliminar: "))
    datos['Usuario'] = [usuario for usuario in usuarios if usuario['UsuarioID'] != id_usuario]
    guardar_datos(datos)
    print("Usuario eliminado exitosamente.")

def buscar_usuario(datos):
    usuarios = datos['Usuario']
    id_usuario = int(input("Ingrese ID del usuario a buscar: "))
    for usuario in usuarios:
        if usuario['UsuarioID'] == id_usuario:
            print(f"ID: {usuario['UsuarioID']}")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Email: {usuario['Email']}")
            print(f"Fecha de Registro: {usuario['FechaRegistro']}")
            return
    print("Usuario no encontrado.")

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
