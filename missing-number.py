from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # prev_nums = {}
        # for num in nums: 
        #     if num in prev_nums:
        #         prev_nums[num] += 1
        #     else:
        #         prev_nums[num] = 1

        # for n in range(len(nums) + 1):  # Fix 3 & 4: check 0..n for absence
        #     if n not in prev_nums:
        #         return n
        n = len(nums)
        intended_sum = n*(n+1)/2
        actual_sum = sum(nums)
        return int(intended_sum - actual_sum)

        # TC : O(N) SC : O(1)