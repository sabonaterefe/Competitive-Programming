class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if node is None:
                return 0
            
            num = num * 10 + node.val
            
            if node.left is None and node.right is None:
                return num
            
            return dfs(node.left, num) + dfs(node.right, num)
        
        return dfs(root, 0)