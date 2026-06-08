from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        
        for num in nums : 
            if num != 0:
                nums[j] = num
                j +=1
        for i in range(j, n):
            nums[i] = 0
        
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12]) 
# Output: [1,3,12,0,0] 
    