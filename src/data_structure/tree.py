class TreeNode:
  def __init__(self, data) -> None:
    self.data = data
    self.left = None
    self.right = None

  def display(self) -> None:
    print(f"Node value: {self.data}")
    
class BinarySearchTree:
  def __init__(self) -> None:
    self.root = None
    
  def __insertNode(self, root: TreeNode, new_node: TreeNode) -> TreeNode:
    if root is None:
      return new_node
    else:
      if new_node.data < root.data: # add on left
        root.left = self.__insertNode(root.left, new_node)
      else:
        root.right = self.__insertNode(root.right, new_node)
    return root
  
  def insert(self, data) -> None:
    new_node = TreeNode(data)
    self.root = self.__insertNode(self.root, new_node)
    
  def __helper_inorder(self, root: TreeNode):  
    if root is not None:
      self.__helper_inorder(root.left)
      print(root.data, end=" ")
      self.__helper_inorder(root.right)
  
  def inorder(self):
    print("inorder")
    self.__helper_inorder(self.root)
      
bst = BinarySearchTree()
bst.insert("maria jose")
bst.insert("Maggie")
bst.insert("leon")
bst.insert("Aloy")

bst.inorder()