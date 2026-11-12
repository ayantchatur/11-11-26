class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def inorderTraversal(root):
    if root.leftNode != None:
        inorderTraversal(root.leftNode)
    print(root.data)
    if root.rightNode != None:
        inorderTraversal(root.rightNode)

def preorderTraversal(root):
    print(root.data)
    if root.leftNode != None:
        preorderTraversal(root.leftNode)
    if root.rightNode != None:
        preorderTraversal(root.rightNode)

def postorderTraversal(root):
    if root.leftNode != None:
        postorderTraversal(root.leftNode)
    if root.rightNode != None:
        postorderTraversal(root.rightNode)
    print(root.data)

root = TreeNode("love")
root.leftNode = TreeNode("The")
root.leftNode.leftNode = TreeNode("hood")

root.rightNode = TreeNode("to")
root.rightNode.leftNode = TreeNode("listen")
root.rightNode.rightNode = TreeNode("jeezy")
root.rightNode.rightNode.rightNode = TreeNode("to")
root.rightNode.rightNode.rightNode.rightNode=TreeNode("and")
root.rightNode.rightNode.rightNode.rightNode.leftNode=TreeNode("weezy")
print("inorder")
inorderTraversal(root)
print("\npreorder")
preorderTraversal(root)
print("\npostorder")
postorderTraversal(root)
