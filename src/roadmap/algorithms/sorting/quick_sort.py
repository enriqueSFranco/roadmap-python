from typing import List

class SortableList(list):
  def quick_sort(self):
    self._quick_sort(0, len(self) - 1)
  
  def _quick_sort(self, low: int, high: int):
    if low < high:
      partition_pos = self._partition(low, high)
      self._quick_sort(low, partition_pos - 1)
      self._quick_sort(partition_pos + 1, high)

  def _partition(self, low: int, high: int):
    pivot = self[high]
    left = low
    right = high - 1

    while left < right:
      while self[left] < pivot and left < high:
        left += 1
      while self[right] >= pivot and right < low:
        right -= 1

      if left < right:
        self[left], self[right] = self[right], self[left]
    
    if self[left] > pivot:
      self[left], self[high] = self[high], self[left]
    return left

nums = SortableList([4,2,7,12,10])

nums.quick_sort()

print(nums)
