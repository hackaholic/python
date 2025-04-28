class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def preorder(root: Node) -> None:
    if root:
        print(f"{root.val}", end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root: Node) -> None:
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"{root.val}", end=" ")

def inorder(root: Node) -> None:
    if root:
        inorder(root.left)
        print(f"{root.val}", end=" ")
        inorder(root.right)
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print("preorder: ")
preorder(root)
print("\n")

print("postorder: ")
postorder(root)
print("\n")

print("inorder: ")
inorder(root)
print("\n")


