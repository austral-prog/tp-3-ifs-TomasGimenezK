def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0

    """

    precioUnidad = float(input())
    cantidad = int(input())
    subtotal = precioUnidad * cantidad


    if cantidad >= 10:
        descuento = 0.2
        monto = subtotal * descuento
        total = subtotal - monto
        print(f"Subtotal: {subtotal}\nDescuento aplicado: {int(descuento * 100)}%\nMonto de descuento: {monto}\nTotal final: {total}")
    elif 10 > cantidad >= 5:
        descuento = 0.1
        monto = subtotal*descuento
        total = subtotal - monto
        print(f"Subtotal: {subtotal}\nDescuento aplicado: {int(descuento*100)}%\nMonto de descuento: {monto}\nTotal final: {total}")
    else:
        descuento = 0
        monto = subtotal * descuento
        total = subtotal - monto
        print(f"Subtotal: {subtotal}\nDescuento aplicado: {int(descuento * 100)}%\nMonto de descuento: {monto}\nTotal final: {total}")


    pass
