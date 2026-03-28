def ordenamiento_agitador_cocktail(arreglo: list[int], ascendente: bool = True) -> list[int]:
    """
    Ordena una lista de enteros usando el algoritmo de Ordenamiento de Agitador de Cocktail

    El algoritmo de Ordenamiento de Agitador de Cocktail es una variación del algoritmo de Ordenamiento Burbuja que recorre la lista
    en ambas direcciones alternativamente, mejorando ligeramente el rendimiento al mover
    tanto los elementos más grandes como los más pequeños hacia sus posiciones correctas
    en cada pasada completa.

    Esta función no modifica la lista original; en cambio, retorna una 
    nueva lista ordenada.

    Argumentos:
        arreglo (list[int]): La lista de enteros a ser ordenada
        ascendente (bool, optional): Si True, ordena la lista en orden ascendente.
            Si False, ordena la lista en orden descendente. Es true predeterminadamente.

    Retorna:
        list[int]: Una nueva lista que contiene los elementos ordenados.
    """

    # Crea una copia de la lista de entrada para evitar modificar la original.
    arr = arreglo.copy()

    # Inicializar los límites para la sección no ordenada de la lista
    inicio = 0
    fin = len(arr) - 1

    # Indicador para rastrear si se realizaron intercambios en un pase
    intercambiado = True

    while intercambiado:
        intercambiado = False

        # Paso hacia adelante: mueve el elemento más grande (o más pequeño) al final.
        for i in range(inicio, fin):
            if (arr[i] > arr[i + 1] and ascendente) or \
               (arr[i] < arr[i + 1] and not ascendente):
                # Intercambiar elementos adyacentes si están en el orden incorrecto.
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intercambiado = True

        # Si no se produjeron intercambios, la lista ya está ordenada.
        if not intercambiado:
            break

        # Reducir el límite superior ya que el último elemento ahora está correctamente ubicado.
        fin -= 1

        intercambiado = False

        # Paso hacia atrás: mueve el elemento más pequeño (o más grande) al inicio.
        for i in range(fin, inicio, -1):
            if (arr[i] < arr[i - 1] and ascendente) or \
               (arr[i] > arr[i - 1] and not ascendente):
                # Intercambiar elementos adyacentes si están en el orden incorrecto.
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                intercambiado = True

        # Aumentar el límite inferior ya que el primer elemento ahora está correctamente ubicado.
        inicio += 1

    return arr
