class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        lis=[]
        for i in range(0,len(blocks)):
            count_b=blocks[i:i+k].count("B") 
            if(count_b>=k):
                return 0
            lis.append(k-count_b)
        return min(lis) 