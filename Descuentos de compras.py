def calcular_descuento(precio, porcentaje_descuento):
    """
    Calcula el descuento aplicado al precio dado un porcentaje de descuento.

    Args:
    precio (float): El precio original del producto.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (en decimal).

    Returns:
    float: El monto del descuento.
    """
    descuento = precio * porcentaje_descuento
    return descuento


def precio_con_descuento(precio, porcentaje_descuento):
    """
    Calcula el precio con el descuento aplicado.

    Args:
    precio (float): El precio original del producto.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (en decimal).

    Returns:
    float: El precio con el descuento aplicado.
    """
    descuento = calcular_descuento(precio, porcentaje_descuento)
    precio_con_descuento = precio - descuento
    return precio_con_descuento


# Ejemplo de uso
precio_original = 100.0
porcentaje_descuento = 0.2  # 20% de descuento

descuento = calcular_descuento(precio_original, porcentaje_descuento)
precio_final = precio_con_descuento(precio_original, porcentaje_descuento)

print("Descuento aplicado:", descuento)
print("Precio final con descuento:", precio_final)
