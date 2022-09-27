class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
        return [-1,-1]
    
    
    # i = 3
    
    # range(1,2) -> [1]
    # j = 2
    