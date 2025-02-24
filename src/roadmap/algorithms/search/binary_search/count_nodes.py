from typing import Optional
from dataclasses import dataclass

@dataclass
class TreeNode:
  def __init__(self, val:int=0, left=None, right=None):
    self.val = val
    self.left:TreeNode = left
    self.right:TreeNode = right

def get_tree_height(root:Optional[TreeNode]):
  if not root:
    return 0
  
  left_depth = get_tree_height(root.left)
  right_depth = get_tree_height(root.right)

  return max(left_depth, right_depth) + 1

def count_nodes(root:Optional[TreeNode]=None) -> int:
  if not root or not(root.left and root.right):
    return root
  
  height = get_tree_height(root)

  if height == 1:
    return 1
  
  return 2**(height -1) - 1

if __name__ == "__main__":
  
    # Representation of the input tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(count_nodes(root))