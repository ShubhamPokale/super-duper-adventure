class Solution:
    
    def findingSingleNumber(self, num):
        # 2 * sum of unique elements - sum of all elements = (Single one number)
        return 2 * sum(set(num)) - sum(num)
    
    
    
s = Solution()
print(s.findingSingleNumber([1,2,3,4,3,2,1]))