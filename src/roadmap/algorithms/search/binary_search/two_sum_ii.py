from typing import List

def two_sum_ii(nums:List[int]=[2,7,11,15], target:int=9) -> List[int]:
  l = 0
  r = len(nums) - 1

  while l < r:
    curr_sum = nums[l] + nums[r]

    if curr_sum == target:
      return [l + 1, r + 1]
    if curr_sum > target:
      r -= 1
    else:
      l += 1

  return [l + 1, r + 1]


def two_sum_ii_binary_search(numbers:List[int]=[2,7,11,15], target:int=9) -> List[int]:
  N = len(numbers)

  for i in range(len(numbers)):
    complement = target - numbers[i]
    l = i + 1
    r = N - 1

    while l <= r:
      mid = l + ((r - l) // 2)
      print(f"mid:{numbers[mid]}")
      if numbers[mid] == complement:
        return [i + 1, mid + 1]

      elif numbers[mid] < complement:
        l = mid + 1
      else:
        r = mid - 1

  return []


# print("usando two pointers")
# print(two_sum_ii([2,7,11,15], 9))
# print(two_sum_ii([-1,0], -1))
# print(two_sum_ii([2,3,4], 6))

print("usando busqueda binaria")
print(two_sum_ii_binary_search([2,7,11,15], 9))
# print(two_sum_ii_binary_search([-1,0], -1))
# print(two_sum_ii_binary_search([1,2,3,4,5], 6))