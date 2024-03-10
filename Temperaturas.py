def convertir_temperatura(grados_centigrados):
  """
  Convierte una temperatura en grados centígrados a grados Fahrenheit y Kelvin.

  Parámetros:
    grados_centigrados (float): La temperatura en grados centígrados.

  Retorno:
    Un diccionario con las siguientes claves:
      "fahrenheit": La temperatura en grados Fahrenheit.
      "kelvin": La temperatura en grados Kelvin.
  """

  fahrenheit = (grados_centigrados * 9/5) + 32
  kelvin = grados_centigrados + 273.15

  return {
    "fahrenheit": fahrenheit,
    "kelvin": kelvin,
  }

# Ejemplo de uso
temperatura_centigrados = 30

resultado = convertir_temperatura(temperatura_centigrados)

print(f"Grados Celsius: {temperatura_centigrados}")
print(f"Grados Fahrenheit: {resultado['fahrenheit']}")
print(f"Grados Kelvin: {resultado['kelvin']}")