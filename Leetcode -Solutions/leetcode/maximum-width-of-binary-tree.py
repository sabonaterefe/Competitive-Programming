from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # (node, position)
        
        while queue:
            level_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, level_width)
            
            for _ in range(len(queue)):
                node, position = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * position))
                
                if node.right:
                    queue.append((node.right, 2 * position + 1))
        
        return max_width