import json

def generar_reporte(datos):
    reporte = {}
    
    for libro in datos['Libro']:
        categoria = libro['Categoria']
        if categoria in reporte:
            reporte[categoria] += 1
        else:
            reporte[categoria] = 1
    
    with open('Reportes_biblioteca_mundo_libro.json', 'w') as archivo:
        json.dump(reporte, archivo, indent=4)
    
    print("Reporte generado exitosamente.")

if _name_ == "_main_":
    try:
        with open('biblioteca.json', 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {"Autor": [], "Categoria": [], "Libro": [], "Usuario": [], "Prestamo": []}
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Se inicializan los datos.")
        datos = {"Autor": [], "Categoria": [], "Libro": [], "Usuario": [], "Prestamo": []}
    generar_reporte(datos)