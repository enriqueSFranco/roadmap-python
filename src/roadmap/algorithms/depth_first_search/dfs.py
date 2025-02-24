"""
------- Algoritmo DFS (Depth First Search) -------
DFS es un algoritmo de búsqueda utilizado para recorrer o buscar a través de estructuras 
de datos como grafos o árboles. Su principio básico es explorar lo más profundo posible 
por cada rama antes de retroceder. En términos simples, va visitando un nodo, luego elige uno 
de sus vecinos no visitados y sigue así hasta llegar a un nodo sin vecinos por explorar. 
Cuando esto sucede, retrocede al nodo anterior y repite el proceso.

------- Pasos básicos de DFS -------
Inicio en el nodo raíz.
Visita el nodo, marcándolo como visitado.
Para cada nodo vecino no visitado del nodo actual, aplica DFS recursivamente.
Si no quedan vecinos por visitar, retrocede a un nodo anterior y repite.
Termina cuando todos los nodos hayan sido visitados.
"""

from typing import Optional


def dfs_iterative(n, edges, source):
    adjacency_list = {i: [] for i in range(n)}

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visited = set()
    stack = [source]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            yield node
            for neighbor in reversed(adjacency_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


def valid_path(n, edges, source, destination):
    """
    Verifica si existe un camino válido entre source y destination en un grafo representado por 'edges'.

    :param n: Número de nodos en grafo
    :param edges: Lista de aristas que representan el grafo
    :param source: Nodo de inicio
    :param destination: Node destino
    :return: True si existe un camino, False de lo contrario
    """
    # creamos la matriz de adyacencia
    # adjacency_matrix = [[0] * n for _ in range(n)]
    graph = {i: [] for i in range(n)}  # lista de adyacencia

    # representamos el grafo como una matriz de adyacencia
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Para un grafo bi-direccional o no dirigido

    visited = set()  # Conjunto para marcar los nodos visitados
    stack = [source]  # stack para almacenar los nodos vecinos

    while stack:
        node = stack.pop()

        if node == destination:
            return True

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # case 1: los nodos q y p son null
    if not p and not q:
        return True

    # case 2: uno de los dos nodos es null y el otro no
    if not p or not q:
        return False

    # case 3: los valores de los nodos son diferentes
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invierte un árbol binario. Este método cambia la posición de los nodos hijos
    izquierdo y derecho de cada nodo en el árbol.

    Args:
    root (Optional[TreeNode]): El nodo raíz del árbol binario.

    Returns:
    Optional[TreeNode]: El nodo raíz del árbol invertido.
    """

    def _invert_node(node: Optional[TreeNode]) -> None:
        if not root:
            return None

        # Intercambiar los subárboles izquierdo y derecho
        root.left, root.right = root.right, root.left

        # Recursivamente invertir los subárboles izquierdo y derecho
        _invert_node(root.left)
        _invert_node(root.right)

    _invert_node(root)
    return root


def is_simmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t1:
            return False
        return (
            (t1.val == t2.val)
            and is_mirror(t1.left, t2.right)
            and is_mirror(t1.right, t2.left)
        )

    return is_mirror(root.left, root.right)


def count_nodes(root: Optional[TreeNode]) -> Optional[int]:
    """
    Dado un árbol binario, cuenta cuántos nodos tiene el árbol.
    """
    if not root:
        return None

    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    n = 3
    # n = 6
    edges = [[0, 1], [1, 2], [2, 0]]
    # edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    # source = 0
    destination = 2
    # destination = 5
    result = valid_path(n, edges, source, destination)
    # result = valid_path(n, edges, source, destination)

    print(result)
