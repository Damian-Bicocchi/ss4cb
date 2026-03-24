def heap_sort(array: list[int], ascendente: bool = True) -> list[int]:
    """
    Ordena una lista de números enteros utilizando el algoritmo "Heap Sort"
    
    Esta función no modifica la lista original; en cambio, retorna una
    nueva lista ordenada.

    Arguments:
        array (list[int]): La lista de números enteros a ser ordenada.
        ascendente (bool, optional): Si True, se ordena de manera ascendente.
            Si False, se ordena de manera descendente. El caso predeterminado es true.

    Retorna:
        list[int]: Una nueva lista que contiene los elementos ordenados.
    """

    # Crear una copia del array para evitar modificar el original
    arr = array.copy()
    n = len(arr)

    def heapify(n: int, i: int):
        """
        Se asegura que el subárbol con raíz en el indice i cumpla con la propiedad de la heap

        Para orden ascendente, construimos una max-heap
        Para orden descendente, construimos una min-heap
        """
        extremo = i  # Inicializamos el más grande o el más chico como la raíz

        izquierdo = 2 * i + 1   # Índice del hijo izquierdo
        derecho = 2 * i + 2  # Índice del hijo derecho

        # Dependiendo del orden de clasificación, elija la comparación
        if ascendente:
            # Construí una max-heap
            if izquierdo < n and arr[izquierdo] > arr[extremo]:
                extremo = izquierdo
            if derecho < n and arr[derecho] > arr[extremo]:
                extremo = derecho
        else:
            # Construi una min-heap
            if izquierdo < n and arr[izquierdo] < arr[extremo]:
                extremo = izquierdo
            if derecho < n and arr[derecho] < arr[extremo]:
                extremo = derecho

        # Si la raíz no es el extremo, intercambia y continua amontonando
        if extremo != i:
            arr[i], arr[extremo] = arr[extremo], arr[i]
            heapify(n, extremo)

    # Paso 1: Construi la heap (max-heap o min-heap)
    # Empezar por el ultimo nodo no-hoja y amontona cada nodo
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Paso 2: Extrae los elementos uno por uno de la heap
    for i in range(n - 1, 0, -1):
        # Mover la raíz actual al final
        arr[i], arr[0] = arr[0], arr[i]

        # Llamar a la función heapify para la heap reducida
        heapify(i, 0)

    return arr
