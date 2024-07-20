def mostrar_menu():
  ruta_base = os.path.dirname(__file__)
  opciones = {
    '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
    # ... (Agregar más opciones)
  }

  while True:
    print("\nMenu Principal - Dashboard")
    for key in opciones:
      print(f"{key} - {opciones[key]}")
    print("0 - Salir")

    eleccion = input("Elige un script para ver su código o '0' para salir: ")

    if eleccion == '0':
      break
    elif eleccion in opciones:
      ruta_script = os.path.join(ruta_base, opciones[eleccion])
      ruta_directorio = os.path.dirname(ruta_script)

      if not verificar_directorio(ruta_directorio):
        print(f"Error: No se encontró el directorio '{ruta_directorio}'.")
      else:
        mostrar_codigo(ruta_script)
    else:
      print("Opción no válida. Por favor, intenta de nuevo.")
