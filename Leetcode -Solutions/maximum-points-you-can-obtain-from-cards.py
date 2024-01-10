class Solution:
    def maxScore(self, cardPoints, k):
        length = len(cardPoints)
        st = length - k
        total_sum = sum(cardPoints[st:st+k])
        res = total_sum
        
        for i in range(k):
            total_sum += cardPoints[i] - cardPoints[st]
            res = max(res, total_sum)
            st += 1
        
        return res