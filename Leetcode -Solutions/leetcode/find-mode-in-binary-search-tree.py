from collections import defaultdict

class Solution:
    def findMode(self, root):
        if not root:
            return []

        modes = []
        count = defaultdict(int)
        max_freq = [0]

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            count[node.val] += 1
            max_freq[0] = max(max_freq[0], count[node.val])

            inorder(node.right)

        inorder(root)

        for key, value in count.items():
            if value == max_freq[0]:
                modes.append(key)

        return modes