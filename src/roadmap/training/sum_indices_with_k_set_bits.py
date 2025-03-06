from typing import List

def count_set_bits(num):
  count = 0
  while num:
    count += num & 1
    num >>= 1 
  return count

def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
  total_sum = 0
  for i, num in enumerate(nums):
    if count_set_bits(i) == k:
      total_sum += num
  return total_sum

print(sumIndicesWithKSetBits([5,10,1,5,2], 1))