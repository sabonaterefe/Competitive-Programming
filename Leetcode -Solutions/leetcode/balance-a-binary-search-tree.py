class Solution:
    def balanceBST(self, root):
        sorted_values = self.inorderTraversal(root)
        return self.constructBST(sorted_values, 0, len(sorted_values) - 1)

    def inorderTraversal(self, root):
        result = []
        self.inorderHelper(root, result)
        return result

    def inorderHelper(self, node, result):
        if node is None:
            return
        self.inorderHelper(node.left, result)
        result.append(node.val)
        self.inorderHelper(node.right, result)

    def constructBST(self, sorted_values, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(sorted_values[mid])
        node.left = self.constructBST(sorted_values, start, mid - 1)
        node.right = self.constructBST(sorted_values, mid + 1, end)

        return node