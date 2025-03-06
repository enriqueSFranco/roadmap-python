from typing import List
from collections import Counter

# https://www.codewars.com/kata/56b4bae128644b5613000037/train/python
def repeat_sum(l: List[List[int]]) -> int:
  count_map = Counter()
  
  for sub_list in l:
    count_map.update(set(sub_list))
  print(count_map)
  ans = sum(num for num, count in count_map.items() if count > 1)
  # for sub_list in l:
  #   unique_elements = set(sub_list)
  #   for element in unique_elements:
  #     count_map[element] = count_map.get(element, 0) + 1
  
  # for number, count in count_map.items():
  #   if count > 1:
  #     answer += number
  return ans

print(repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]]))
print(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]))
print(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]))

