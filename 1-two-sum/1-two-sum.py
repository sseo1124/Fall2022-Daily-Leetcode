class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, e in enumerate(nums):
            v = target - e
            
            if v in d:
                return [d[v], i]
            else:
                d[e] = i
            
        
        return [-1,-1]