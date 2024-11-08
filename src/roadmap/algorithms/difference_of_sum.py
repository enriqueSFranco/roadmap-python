from typing import List

# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
  def __get_sum_digit(self, num: int) -> int:
    sum: int = 0
    
    if num > 9:
      while num:
        sum += num % 10
        num //= 10
    
      return sum
    return num
  
  def difference_of_sum(self, nums: List[int]) -> int:
    sum_elements, sum_digits = 0, 0
    
    for num in nums:
      sum_digits += self.__get_sum_digit(num)
      sum_elements += num
    
    return abs(sum_elements - sum_digits)
  
solution = Solution()

print(solution.difference_of_sum([1, 15, 6, 3]))