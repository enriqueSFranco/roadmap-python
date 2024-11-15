from dataclasses import dataclass

@dataclass
class TreeNode:
  def __init__(self, val:int=0, left=None, right=None):
    self.val = val
    self.left:TreeNode = left
    self.right:TreeNode = right
