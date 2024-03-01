from typing import Optional

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def dfs(node):
            nonlocal max_sum

            if not node:
                return (True, 0, float('inf'), float('-inf'))

            left_bst, left_sum, left_min, left_max = dfs(node.left)
            right_bst, right_sum, right_min, right_max = dfs(node.right)

            if (
                left_bst
                and right_bst
                and left_max < node.val < right_min
            ):
                curr_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, curr_sum)
                return (True, curr_sum, min(left_min, node.val), max(right_max, node.val))

            return (False, 0, float('-inf'), float('inf'))

        dfs(root)
        return max_sum