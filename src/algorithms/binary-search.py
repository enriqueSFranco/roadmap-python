from typing import List

class BinarySearch:
  def maximumCount(self, nums: List[int]) -> int:
    N = len(nums)
    if nums[0] > 0 or nums[N - 1] < 0:
      return N
    
    def search(target: int) -> int:
      low, high = 0, N - 1
      
      while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
          high = mid
        else:
          low = mid + 1
      return low

    indexZero = search(0)
    indexOne = search(1)
    
    return max(indexZero, N - indexOne)
  

binarySearch = BinarySearch()
print(binarySearch.maximumCount([-2,-1,-1,1,2,3]))