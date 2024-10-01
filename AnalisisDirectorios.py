"""
Quiz 1, programación.
Vianca Navarro.
Scripting.
"""

import os
import sys

def archivos1(directorio): #La función verifica si el directorio existe mediante el path.exist.
    informacion_archivos = []
    if not os.path.exists(directorio):
        print("Directorio no encontrado.")
        return
    txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')] #Mediante el endswith txt, se pueden 
    #leer y encontrar los archivos .txt en el directorio.
    if not txt:
        with open(os.path.join(directorio, 'informe.txt'), 'w') as informe:
            informe.write("No existen archivos .txt en el directorio.")
        print("No se encontraron archivos .txt")
        return
    for archivo in txt:
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, 'r') as f: #Se lee cada archivo .txt separándolo por líneas y se añade la información.
            contenido = f.readlines()
            num_lineas = len(contenido)
            num_palabras = sum(len(linea.split()) for linea in contenido)
            num_python = sum(linea.lower().count('python') for linea in contenido)
            informacion_archivos.append({
                'nombre': archivo,
                'lineas': num_lineas,
                'palabras': num_palabras,
                'python': num_python
            })

    with open(os.path.join(directorio, 'archivo2.txt'), 'w') as archivo2: #Formación de un archivo .txt y su información.
        for info in informacion_archivos:
            archivo2.write(f"Nombre del archivo: {info['nombre']}\n")
            archivo2.write(f"Número de líneas: {info['lineas']}\n")
            archivo2.write(f"Número total de palabras: {info['palabras']}\n")
            archivo2.write(f"Número de veces que aparece la palabra 'Python': {info['python']}\n")
            archivo2.write("\n")

    print("El archivo se generó correctamente. Archivo generado en 'archivo2.txt'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Modo de uso: python script.py <directorio>")
    else:
        directorio = sys.argv[1]
        archivos1(directorio)
