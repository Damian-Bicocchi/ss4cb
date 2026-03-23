import heapq

def heuristica(nodo, destino):
    """Estima el costo desde el nodo hasta el destino usando la distancia Manhattan."""
    return abs(nodo[0] - destino[0]) + abs(nodo[1] - destino[1])

def busqueda_aestrella(grafo, inicio, destino):
    """
    Encuentra el camino más corto desde inicio hasta destino usando el algoritmo A*.

    grafo:   dict que mapea cada nodo a una lista de tuplas (vecino, costo)
    inicio:  nodo de partida
    destino: nodo objetivo

    Retorna el camino más corto como lista de nodos, o None si no existe camino.
    """
    conjunto_abierto = []
    heapq.heappush(conjunto_abierto, (0, inicio))

    vino_de = {}
    puntaje_g = {inicio: 0}
    puntaje_f = {inicio: heuristica(inicio, destino)}

    while conjunto_abierto:
        f_actual, nodo_actual = heapq.heappop(conjunto_abierto)

        if nodo_actual == destino:
            return reconstruir_camino(vino_de, nodo_actual)

        for vecino, costo_arista in grafo.get(nodo_actual, []):
            g_tentativo = puntaje_g[nodo_actual] + costo_arista

            if g_tentativo < puntaje_g.get(vecino, float('inf')):
                vino_de[vecino] = nodo_actual
                puntaje_g[vecino] = g_tentativo
                puntaje_f[vecino] = g_tentativo + heuristica(vecino, destino)
                heapq.heappush(conjunto_abierto, (puntaje_f[vecino], vecino))

    return None  # No se encontró camino

def reconstruir_camino(vino_de, nodo_actual):
    """Reconstruye el camino siguiendo los punteros de vino_de hasta el inicio."""
    camino = [nodo_actual]
    while nodo_actual in vino_de:
        nodo_actual = vino_de[nodo_actual]
        camino.append(nodo_actual)
    camino.reverse()
    return camino
