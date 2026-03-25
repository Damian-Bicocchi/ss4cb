def euclides_mcd(primer_numero: int, segundo_numero: int) -> int:
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos
    utilizando el algoritmo de Euclides basado en restas.

    Args:
        primer_numero (int): Primer número entero positivo.
        segundo_numero (int): Segundo número entero positivo.

    Returns:
        int: El MCD de primer_numero y segundo_numero.

    Raises:
        ValueError: Si primer_numero o segundo_numero es cero o negativo.
    """
    # Valida que ambos valores sean enteros estrictamente positivos;
    # el MCD no está definido para el cero ni para números negativos.
    if primer_numero <= 0 or segundo_numero <= 0:
        raise ValueError(
            "Ambos números deben ser enteros estrictamente positivos (> 0). "
            f"Recibido: primer_numero={primer_numero}, segundo_numero={segundo_numero}."
        )

    # Sigue iterando mientras los dos valores sean distintos.
    # Cuando son iguales, ese valor es el MCD.
    while primer_numero != segundo_numero:

        if primer_numero > segundo_numero:
            # Si primer_numero es mayor, reemplazarlo con la diferencia (primer_numero - segundo_numero).
            # Esto refleja: MCD(primer_numero, segundo_numero) = MCD(primer_numero - segundo_numero, segundo_numero)
            primer_numero = primer_numero - segundo_numero
        else:
            # Si segundo_numero es mayor (o podrían ser iguales, manejado por la condición while),
            # Reemplazar el segundo número con la diferencia  (segundo_numero - primer_numero).
            # Esto refleja: MCD(primer_numero, segundo_numero) = MCD(primer_numero, segundo_numero - primer_numero)
            segundo_numero = segundo_numero - primer_numero

    # En este punto, primer_numero == segundo_numero, por lo que cualquiera de las dos variables contiene el MCD.
    return primer_numero