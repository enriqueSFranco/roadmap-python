from typing import List

def merge_sort(array) -> List[int]:
  N = len(array)
  if N == 1:
    return array

  left = 0
  right = N - 1
  middle = left + (right - left) // 2
  left_array = array[:middle + 1]
  right_array = array[middle + 1:]

  sorted_left_array = merge_sort(left_array)
  sorted_right_array = merge_sort(right_array)
  
  return merge(sorted_left_array, sorted_right_array)

def merge(left_array: List[int], right_array: List[int]) -> List[int]:
  sorted_array: List[int] = []

  while len(left_array) > 0 and len(right_array) > 0:
    if left_array[0] > right_array[0]:
      sorted_array.append(right_array[0])
      right_array.pop(0)
    else:
      sorted_array.append(left_array[0])
      left_array.pop(0)

  
  while len(left_array) > 0:
    sorted_array.append(left_array[0])
    left_array.pop(0)

  while len(right_array) > 0:
    sorted_array.append(right_array[0])
    right_array.pop(0)
    
  return sorted_array


nums = [4,7,3,10,2]
print(merge_sort(nums))
# encontrar el indice del elemento de enmedio