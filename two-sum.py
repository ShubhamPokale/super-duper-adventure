# The Challenge:
# You have a list of numbers: nums = [2, 7, 11, 15] and a target = 9.
# You want to find if any two numbers add up to that target.
from typing import List
nums = [5,8,2]
target = 10

# #brute force solution
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]      
            
# print(two_sum(nums, target))                     

# #solution:

# # count = {}
# # def two_sum_prime(nums, target):
# #     for num in nums:# [2, 7, 11, 15] target = 9.
# #         if num in count: 
# #             count[num] = count[num] + 1
# #         else:
# #             count[num] = 1 # 2:1, 7:1 11:1 15 :1
# #         if target - num in count:
# #             return [nums.index(num), nums.index(target - num)]
        
# # print(two_sum_prime(nums, target))


# print("Optimized output:")
# #optimized

# def two_sim_final(nums, target):
#     prev_map ={} # n, i
    
#     for i,n in enumerate(nums):
#         diff = target -n
#         if diff in prev_map:
#             return [prev_map[diff], i]
#         else :
#             prev_map[n] = i
            
            
# print(two_sim_final(nums, target)) 
    
    
class Solution:
    def twoSum(self, nums: List[int], target: int):
        prev_nums = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in prev_nums:
                return [prev_nums[diff], i]
            else:
                prev_nums[n] = i
                
s= Solution()
print(s.twoSum(nums, target))