class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node, prev):
            if node is None:
                return prev
            prev = inorder(node.left, prev)
            if prev is None or node.val <= prev:
                return None
            return inorder(node.right, node.val)

        return inorder(root, float('-inf')) is not None