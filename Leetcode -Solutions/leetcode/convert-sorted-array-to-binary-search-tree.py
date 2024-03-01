class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(start, end):
            if start > end:
                return None

            middle = (start + end) // 2
            root = TreeNode(nums[middle])
            root.left = buildBST(start, middle - 1)
            root.right = buildBST(middle + 1, end)
            return root

        return buildBST(0, len(nums) - 1)