from dataclasses import dataclass
from typing import List

@dataclass
class ListNode:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

class Solution:
  def sort_list_bf(self, head: ListNode) -> ListNode:
    # brute force approach (this works fine)
    array_list = []

    curr_node = head
    while curr_node is not None:
      array_list.append(curr_node.data)
      curr_node = curr_node.next

    sorted_array = sorted(array_list)

    temp = head
    for item in sorted_array:
      temp.data = item
      temp = temp.next

    return head

  def merge_sort(self, head: ListNode) -> ListNode:
    return self._merge_sort(head)

  def _merge_sort(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head

    # Divide the list into two halves
    middle: ListNode = self._search_middle_node(head)
    left_half = head
    right_half = middle.next
    middle.next = None  # We break the connection between the halves

    # Recursively sort both halves
    sorted_left = self._merge_sort(left_half)
    sorted_right = self._merge_sort(right_half)

    # Merge the sorted halves
    return self._merge(sorted_left, sorted_right)

  def _merge(self, left_ll: ListNode, right_ll: ListNode) -> ListNode:
    # Merge two sorted linked lists
    if not left_ll:
      return right_ll
    if not right_ll:
      return left_ll

    if left_ll.data < right_ll.data:
      result = left_ll
      result.next = self._merge(left_ll.next, right_ll)
    else:
      result = right_ll
      result.next = self._merge(left_ll, right_ll.next)

    return result

  def _search_middle_node(self, head: ListNode) -> ListNode:
    # Using slow and fast pointers to find the middle of the linked list
    if head is None or head.next is None:
      return head
    slow = head
    fast = head.next  # We move fast one step ahead to ensure slow gets the middle
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow

  def print_linked_list(self, head: ListNode) -> None:
    curr_node = head
    while curr_node is not None:
      if curr_node.next is not None:
        print(f"{curr_node.data}->", end="")
      else:
        print(curr_node.data)
      curr_node = curr_node.next

  def create_linked_list(self, array_list: List[int]) -> ListNode:
    dummy = ListNode()
    curr = dummy

    for value in array_list:
      curr.next = ListNode(value)
      curr = curr.next
    return dummy.next

# Test the solution
solution = Solution()
nums = [200, 3, 2, 5, 4, 1, 9, 100]
head = solution.create_linked_list(nums)

# Sorting the linked list using merge sort
head = solution.merge_sort(head)

# Printing the sorted linked list
solution.print_linked_list(head)
