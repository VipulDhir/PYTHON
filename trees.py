class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
   if root is None:
      return Node(data)
   else:
      if data < root.data:
         root.left = insert(root.left, data)
      else:
         root.right = insert(root.right, data)
   return root


def inorder_traversal(root):
   if root:
      inorder_traversal(root.left)
      print(root.data, end=" ")
      inorder_traversal(root.right)

def preorder_traversal(root):
   if root:
      print(root.data, end=" ")
      preorder_traversal(root.left)
      preorder_traversal(root.right)

def postorder_traversal(root):
   if root:
      preorder_traversal(root.left)
      preorder_traversal(root.right)
      print(root.data, end=" ")

# Usage example
root_node = None

# Inserting elements into the binary tree
root_node = insert(root_node, 5)
root_node = insert(root_node, 3)
root_node = insert(root_node, 7)
root_node = insert(root_node, 1)
root_node = insert(root_node, 4)

# Traversing the binary tree
print("Inorder Traversal:",)
inorder_traversal(root_node)

print("preorder Traversal:")
preorder_traversal(root_node)

print("postorder Traversal:")
postorder_traversal(root_node)




