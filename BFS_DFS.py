class TreeNode:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.right = right
        self.left = left


def BFS(root):
    if not root:
        return

    queue = [root]

    while queue:

        node = queue.pop(0)

        print(node.val,end=' ')

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def DFS_recursive(root):

    if not root:
        return

    print(root.val,end= ' ')

    DFS_recursive(root.left)
    DFS_recursive(root.right)





if "__main__" == __name__:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    BFS(root)
    print()
    DFS_recursive(root)
