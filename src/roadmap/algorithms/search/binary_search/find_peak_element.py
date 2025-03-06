from typing import List

def find_peak_element(nums: List[int]) -> int:
  N = len(nums)
  left = 0
  right = N - 1

  while left < right:
    mid = left + ((right - left) // 2)

    if nums[mid] < nums[mid + 1]:
      left = mid + 1
    else:
      right = mid
  
  return left
nums = [1,2]
print(find_peak_element(nums))
