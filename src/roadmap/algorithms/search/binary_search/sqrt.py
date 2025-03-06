from math import floor
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

logger = logging.getLogger("loggerMySqrt")

def my_sqrt_iterative(x: int) -> int:
  left = 0
  right = x

  while left <= right:
    if x == 0:
      return 0
    mid = floor(left + (right - left) / 2)

    if x == mid * mid:
      return mid
    if mid * mid < x:
      left = mid + 1
    else:
      right = mid - 1
  return right

logger.debug(my_sqrt_iterative(25))

def helper_my_sqrt(x: int, left:int, right:int=None) -> int:
  if x == 0:
    return 0

  if right is None:
    right = x

  if left > right:
    return right
  
  mid = floor(left + (right - left) / 2)
  
  if mid * mid == x:
    return mid
  if mid * mid < x:
    return helper_my_sqrt(x,mid+1,right)
  else:
    return helper_my_sqrt(x,left,mid-1)

def my_sqrt(x:int) -> int:
  return helper_my_sqrt(x, 0)

logger.debug(my_sqrt(625))