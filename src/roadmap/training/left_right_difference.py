from typing import List

class Soulution:
  def __left_sum(self, nums: List[int]) -> List[int]:
    collection: List[int] = [0] * len(nums)
    
    for i in range(1, len(nums)):
      collection[i] = collection[i - 1] + nums[i - 1]
      
    return collection
    
  
  def __right_sum(self, nums: List[int]) -> List[int]:
    collection: List[int] = [0] * len(nums)
    
    for i in range(len(nums) - 2, -1, -1):
      collection[i] = collection[i + 1] + nums[i + 1]
      
    return collection
  
  def leftRightDifference(self, nums: List[int]) -> List[int]:
    answer: List[int] = [0] * len(nums)
    
    for i in range(0, len(nums)):
      answer[i] = abs(self.__left_sum(nums)[i] - self.__right_sum(nums)[i])
      
    return answer
  
solution = Soulution()
print(solution.leftRightDifference([10, 4, 8, 3]))