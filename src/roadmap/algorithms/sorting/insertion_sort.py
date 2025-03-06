from dataclasses import dataclass
from typing import List, Optional


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
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = str(self.val)
        if self.next:
            result += "->" + repr(self.next)
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
        curr.next = None  # Desconectamos el nodo de la lista original

        # insertamos 'curr' a la lista ordenada
        if not sorted_head or curr.val <= sorted_head.val:
            # case 1: insertar al inicio de la lista
            curr.next = sorted_head  # "desconectamos" el nodo curr de la lista desordenada y lo colocamos en la lista "sorted_head"
            sorted_head = curr  # actualizamos "sorted_head" para que apunte a curr
        else:
            # case 2: buscar en que posicion de la lista ordenada debemos insetar el nodo 'curr'
            sorted_pos = sorted_head
            while sorted_pos.next and sorted_pos.next.val < curr.val:
                sorted_pos = sorted_pos.next

            # insertamos el nodo "curr" justo despues del nodo "sorted_pos"
            curr.next = sorted_pos.next
            sorted_pos.next = curr
        curr = next_node  # avanzamos al siguiente nodo de la lista desornedad

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
