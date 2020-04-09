# tree travesal in inorder , preorder and postorder
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.val)
            self.Inorder(root.right)
    def Preorder(self,root):
        if root:
            print(root.val)
            self.Preorder(root.left)
            self.Preorder(root.right)
    def Postorder(self,root):
        if root:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.val)

root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
root.right.right=Node("G")
root.left.left.left=Node("H")
root.left.left.right=Node("I")
root.left.right.left=Node("J")
root.left.right.right=Node("K")
print("Inorder traversal of binary tree is ")
root.Inorder(root)
print("\nPreorder traversal of binary tree is ")
root.Preorder(root)
print("\nPostorder traversal of binary tree is ")
root.Postorder(root)