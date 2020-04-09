class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)

def printDepthFirst(root):
    h = height(root)
    for i in range (1, h+1):
        printLevel(root, i)

def printLevel(root, level):
    if root is None:
        return
    if level==1:
        print(root.data)
    elif level>1:
        printLevel(root.left, level-1)
        printLevel(root.right, level-1)

def height(node):                        #function to define the height of the tree
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight> rheight:
            return lheight+1
        else :
            return rheight+1

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(9)
root.left.right = Node(18)
root.right.left = Node(28)
root.right.right = Node(35)
root.left.left.left = Node(7)
root.left.left.left.left = Node(5)
root.right.right.left = Node(33)
root.right.right.right = Node(40)
root.left.right.left = Node(16)


print("Defth first level traversal of binary tree is")
printDepthFirst(root)

print("Post Order traversal: ")
root.PostOrder(root)