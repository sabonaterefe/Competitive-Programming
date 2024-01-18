class Solution:
    def intervalIntersection(self, A, B):
        i, j, ans = 0, 0, []
        
        while i < len(A) and j < len(B):
            curr = [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]
            if curr[0] <= curr[1]:
                ans.append(curr)
            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1

        return ans