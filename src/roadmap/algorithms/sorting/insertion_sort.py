from typing import List, Optional
from dataclasses import dataclass

def insertion_sort(arr: List[int]):
  N = len(arr)
  if N == 1:
    return arr
  
  if N == 2:
    if arr[0] < arr[1]:
      return arr
    else:
      arr[0], arr[1] = arr[1], arr[0]

  for i in range(1, N):
    curr_value = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > curr_value:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = curr_value

@dataclass
class ListNode:
  def __init__(self, val: int=0, next=None):
    self.val = val
    self.next = next

  def __repr__(self):
    result = str(self.val)
    if self.next:
      result += '->' + repr(self.next)
    return result

def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head
  
  sorted_head: Optional[ListNode] = None
  curr = head
  while curr:
    # En cada iteración, 'curr' es el nodo a insertar
    # Guardamos el siguiente nodo de 'curr' antes de cambiar nada
    next_node: ListNode = curr.next
    curr.next = None # Desconectamos el nodo de la lista original

    # insertamos 'curr' a la lista ordenada
    if not sorted_head or curr.val <= sorted_head.val:
      # case 1: insertar al inicio de la lista
      curr.next = sorted_head # "desconectamos" el nodo curr de la lista desordenada y lo colocamos en la lista "sorted_head"
      sorted_head = curr # actualizamos "sorted_head" para que apunte a curr
    else:
      # case 2: buscar en que posicion de la lista ordenada debemos insetar el nodo 'curr'
      sorted_pos = sorted_head
      while sorted_pos.next and sorted_pos.next.val < curr.val:
        sorted_pos = sorted_pos.next

      # insertamos el nodo "curr" justo despues del nodo "sorted_pos"
      curr.next = sorted_pos.next
      sorted_pos.next = curr
    curr = next_node # avanzamos al siguiente nodo de la lista desornedad
  
  return sorted_head

def create_list(array: List[int]) -> Optional[ListNode]:
  dummy = ListNode(-1)
  curr = dummy

  for val in array:
    curr.next = ListNode(val)
    curr = curr.next

  return dummy.next

def print_linked_list(head: Optional[ListNode]) -> None:
  curr = head
  while curr:
    if curr.next:
      print(f"{curr.val}->", end="")
    else:
      print(curr.val)
    curr = curr.next


nums = [2, 6, 1, 10, 5, 2]
head = create_list(nums)

# Imprime la lista desordenada
print("Lista desordenada:")
print_linked_list(head)

# Ordena la lista
sorted_head = insertion_sort_list(head)

# Imprime la lista ordenada
print("Lista ordenada:")
print_linked_list(sorted_head)

"""
¡Sí! El problema que describes es exactamente la aplicación del algoritmo de **Insertion Sort** en una lista enlazada simple (singly linked list). Aquí el objetivo es ordenar una lista enlazada, utilizando el enfoque clásico de **Insertion Sort**, donde iteras a través de la lista, tomas un elemento a la vez, y lo insertas en su lugar adecuado en la lista ya ordenada.

A continuación, te proporciono una **implementación detallada** en Python, que resuelve este problema de la manera que describes.

### Implementación de Insertion Sort en una lista enlazada

Para este algoritmo, lo que haremos es:
1. Iterar por cada nodo de la lista.
2. Insertar el nodo actual en la posición correcta dentro de una lista ordenada.
3. A medida que avanzamos, la lista ordenada crecerá y la lista original irá quedando vacía.

El código en Python sería algo como esto:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: ListNode) -> ListNode:
    # La lista ordenada estará representada por 'sorted_head'
    sorted_head = None
    
    # Iterar sobre la lista original
    current = head
    while current:
        # En cada iteración, 'current' es el nodo a insertar
        # Guardamos el siguiente nodo de 'current' antes de cambiar nada
        next_node = current.next
        current.next = None  # Desconectamos el nodo de la lista original
        
        # Insertamos 'current' en la lista ordenada
        if not sorted_head or current.val <= sorted_head.val:
            # Caso 1: Insertamos al inicio de la lista ordenada
            current.next = sorted_head
            sorted_head = current
        else:
            # Caso 2: Encontramos el lugar adecuado para insertarlo
            sorted_pos = sorted_head
            while sorted_pos.next and sorted_pos.next.val < current.val:
                sorted_pos = sorted_pos.next
            # Insertamos el nodo después de 'sorted_pos'
            current.next = sorted_pos.next
            sorted_pos.next = current
        
        # Avanzamos al siguiente nodo en la lista original
        current = next_node
    
    # Al final, 'sorted_head' es la cabeza de la lista ordenada
    return sorted_head
```

### Explicación del código:

1. **Clase ListNode**: Define la estructura del nodo de la lista enlazada. Cada nodo tiene un valor (`val`) y un puntero al siguiente nodo (`next`).

2. **Función `insertionSortList`**: 
   - Inicializamos la variable `sorted_head`, que representa la cabeza de la lista ya ordenada. Empezamos con `None` porque al principio no hay nodos ordenados.
   - Usamos un bucle `while` para iterar sobre cada nodo de la lista original.
   - Por cada nodo de la lista original, desconectamos su puntero `next` para que no afecte el proceso de ordenación.
   - Luego, insertamos ese nodo en la posición adecuada dentro de la lista ordenada. Para ello, recorremos la lista ordenada (almacenada en `sorted_head`) y encontramos el lugar adecuado para insertar el nodo actual.
   - Finalmente, avanzamos al siguiente nodo en la lista original (`current = next_node`).

3. **Casos de inserción**:
   - Si la lista ordenada está vacía o el nodo actual es más pequeño que el primer nodo de la lista ordenada, lo insertamos al principio.
   - En el caso contrario, buscamos el lugar adecuado para insertarlo en la lista ordenada.

4. **Resultado**: Al final, la lista ordenada estará representada por `sorted_head`, que es la cabeza de la lista ya ordenada.

### Ejemplo de uso

Supongamos que tienes la siguiente lista:

```
4 -> 3 -> 1 -> 5 -> 2
```

Puedes crear los nodos y usar la función `insertionSortList` de la siguiente forma:

```python
# Crear la lista enlazada 4 -> 3 -> 1 -> 5 -> 2
head = ListNode(4)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(2)

# Ordenar la lista
sorted_head = insertionSortList(head)

# Imprimir la lista ordenada
current = sorted_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
```

La salida sería:

```
1 -> 2 -> 3 -> 4 -> 5
```

### Complejidad:

- **Tiempo**: La complejidad temporal en el peor caso es **O(n²)**, donde **n** es el número de nodos en la lista. Esto se debe a que, en cada iteración, en el peor de los casos, tenemos que recorrer toda la lista ordenada para encontrar la posición de inserción del nodo actual.
  
- **Espacio**: La complejidad espacial es **O(1)**, ya que estamos manipulando la lista in-place (sin usar estructuras de datos adicionales como listas o arreglos).

### Conclusión

Este es el algoritmo de **Insertion Sort** aplicado a una lista enlazada simple, que es precisamente el problema que deseas resolver. Aunque la complejidad es cuadrática y no es el algoritmo más eficiente para listas grandes, es bastante útil para listas pequeñas o listas que ya están parcialmente ordenadas.








Claro, para explicar de manera gráfica lo que hace este fragmento de código:

```python
curr.next = sorted_head
sorted_head = curr
```

Vamos a ver qué ocurre paso a paso. Imagina que tienes una lista vinculada (linked list) que se está ordenando mediante el algoritmo de **insertion sort**. El objetivo de este fragmento es insertar el nodo `curr` al principio de la lista ordenada `sorted_head`. Aquí te lo explico visualmente:

### Estado inicial

Supongamos que tienes dos listas vinculadas:

- `sorted_head`: Es la cabeza de la lista ordenada.
- `curr`: Es el nodo que estamos intentando insertar en la lista ordenada.

#### Antes de ejecutar las instrucciones

```
sorted_head --> [2] --> [5] --> [8] --> None  # Lista ordenada
curr        --> [1] --> None  # Nodo a insertar
```

### 1. `curr.next = sorted_head`

Esta línea lo que hace es conectar el nodo `curr` al principio de la lista ordenada. Es decir, le asigna al campo `next` de `curr` la dirección de la lista ordenada (`sorted_head`). Esto "desconecta" a `curr` de cualquier otra parte, pero lo coloca al inicio de la lista ordenada.

**Efecto visual:**

```
curr.next = sorted_head
```

Después de esta operación, `curr` apunta a `sorted_head`.

```
sorted_head --> [2] --> [5] --> [8] --> None  # Lista ordenada
curr        --> [1] --> [2] --> [5] --> [8] --> None  # 'curr' ahora apunta a 'sorted_head'
```

### 2. `sorted_head = curr`

Esta línea cambia el valor de `sorted_head` para que apunte a `curr`. Es decir, estamos actualizando la cabeza de la lista ordenada para que ahora sea el nodo `curr`, porque hemos insertado `curr` al principio.

**Efecto visual:**

```
sorted_head = curr
```

Después de esta operación, `sorted_head` ahora apunta a `curr`, y la lista ordenada comienza con `curr`.

```
sorted_head --> [1] --> [2] --> [5] --> [8] --> None  # Ahora 'curr' es el nuevo 'sorted_head'
curr        --> [1] --> [2] --> [5] --> [8] --> None  # 'curr' sigue igual, pero ahora es la cabeza de la lista ordenada
```

### Resumen visual

Lo que estás haciendo en este fragmento es:

1. **Conectar** `curr` al inicio de la lista ordenada.
2. **Actualizar** `sorted_head` para que apunte a `curr`, haciendo de él el primer nodo de la lista ordenada.

La operación efectivamente inserta el nodo `curr` en la posición correcta al principio de la lista ordenada en cada iteración del algoritmo de **insertion sort**.

Si tienes alguna duda adicional, no dudes en preguntarme.
"""