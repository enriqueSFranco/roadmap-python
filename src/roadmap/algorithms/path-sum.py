from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Soultion:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(node: TreeNode, curr_sum: int) -> bool:
      if not node: # si es None
        return False
      
      curr_sum += node.val # 5
      if not node.left and not node.right:
        return curr_sum == targetSum
      return (dfs(node.left, curr_sum) or dfs(node.right, curr_sum))
    
    return dfs(root, 0)
  
  def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(node: TreeNode):
      if not node: return 0
      
      if node.val >= low and node.val <= high:
        curr_sum += node.val
      if node.val < low:
        curr_sum += dfs(node.right)
      if  node.val > high:
        curr_sum += dfs(node.left)
      return curr_sum
    return dfs(root)
  
# 5,4,8,11,null,13,4,7,2,null,null,null,1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

ans = Soultion()
print(ans.hasPathSum(root, 22))