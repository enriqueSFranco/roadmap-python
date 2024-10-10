from typing import List

def binary_search(arr: List[int], key: int) -> int:
  low, high = 0, len(arr) - 1
  answer = -1
  
  while low <= high:
    middle = low + (high - low) // 2
    
    if arr[middle] <= key:
      answer = middle
      low = middle + 1
    else:
      high = middle - 1
      
  return answer

class Prefix:
  def fill_prefix_sum(self, arr: list[int]):
    N = len(arr)
    prefix_sum = [0] * N
    prefix_sum[0] = arr[0]
    
    for i in range(1, N):
      prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum
  
  def answer_queries(self, nums: List[int], queries: List[int]) -> List[int]:
    nums_sorted = sorted(nums)
    N = len(nums_sorted)
    prefix_sum = [0] * N
    prefix_sum[0] = nums_sorted[0]
    
    for i in range(1, N):
      prefix_sum[i] = prefix_sum[i - 1] + nums_sorted[i]
      
    answer: List[int] = [0] * len(queries)
    for i in range(len(queries)):
      query = queries[i]
      index = binary_search(prefix_sum, query)
      answer[i] = index + 1 if index != -1 else 0
           
    return answer
  
  
prefix = Prefix()
print(prefix.answer_queries([4,5,2,1], [3,10,21]))
# print(prefix.fill_prefix_sum([3, 2, 1, 3, 1, 4, 2]))


class NumArray:
  def __init__(self, nums: List[int]):
    self.__psums = self.__fill_prefix_sum(nums)
  
  def __fill_prefix_sum(self, arr: List[int]) -> List[int]:
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    
    for i in range(1, len(arr)):
      prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum
        
  def sum_range(self, left: int, right: int) -> int:
    if left < 0 or right > len(self.__psums):
      return
    
    if left == 0:
      return self.__psums[right]
    return self.__psums[right] - self.__psums[left - 1]

arr = [-2, 0, 3, -5, 2, -1] # prefix sum = [-2, -2, 1, -4, -2, -3]
num_array = NumArray(arr)
print(num_array.sum_range(0, 2))
print(num_array.sum_range(2, 5))
print(num_array.sum_range(0, 0))
