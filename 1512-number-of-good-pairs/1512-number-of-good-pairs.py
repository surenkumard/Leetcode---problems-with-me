class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        dic = {}
        for i in nums:
            if i in dic:
                pairs += dic[i] 
                dic[i] += 1
            else:
                dic[i] = 1
        return pairs
                
        