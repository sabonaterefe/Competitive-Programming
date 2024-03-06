class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top_index = stack.pop()
                height = heights[top_index]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

        while stack:
            top_index = stack.pop()
            height = heights[top_index]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area