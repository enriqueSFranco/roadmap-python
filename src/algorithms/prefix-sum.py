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
