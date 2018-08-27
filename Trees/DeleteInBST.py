class TreeNode:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def preOrderTraversal(root):
  if root is None: return
  print(root.val,end = " ")
  preOrderTraversal(root.left)
  preOrderTraversal(root.right) 

class Solution:
  def deleteInBST(self, root, target):
    if root is None: return root
    elif root.val < target:
      root.right = self.deleteInBST(root.right, target)
      return root
    elif root.val > target:
      root.left = self.deleteInBST(root.left, target)
      return root
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      else:
        if root.right.left is None:
          root.right.left = root.left
          return root.right
        else:
          replaceNode = self.smallestNode(root.right)
          replaceNode.left = root.left
          replaceNode.right = root.right
          return replaceNode

  def smallestNode(self, root):
    prev = root
    cur = root
    while cur.left:
      prev = cur
      cur = cur.left
    prev.left = None
    return cur

# Testcases
def main():
  solution = Solution()
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(7)
  root.right.left = TreeNode(6)
  root.right.left.left = TreeNode(5)
  root.right.right = TreeNode(9)
  preOrderTraversal(root)
  print()
  root = solution.deleteInBST(root, 6)
  preOrderTraversal(root)
  print()
  root = solution.deleteInBST(root, 4) 
  preOrderTraversal(root)
  print()

main()
