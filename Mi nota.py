# Escritura de Archivo de Texto
# Abre el archivo en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribe al menos tres líneas de notas personales
    file.write("Estas son mis notas personales:\n")
    file.write("- Recordar comprar leche en el supermercado.\n")
    file.write("- Llamar a Jessy para confirmar la reunión.\n")
    file.write("- Preparar la presentación para el martes.\n")
    file.write("- LLegar puntual al trabajo.\n ")

# Lectura de Archivo de Texto
# Abre el archivo en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra en la consola cada línea leída
        print(line.strip())

# El archivo se cerrará automáticamente al salir del bloque 'with