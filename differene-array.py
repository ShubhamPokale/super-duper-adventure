class Solution:
    # def findDifferenceArray(self, nums):
    #     n = len(nums)
    #     differenceArray = [0] * n
    #     leftSum = 0
    #     rightSum = sum(nums)

    #     # Calculate the difference between left and right sums for each position
    #     for i in range(n):
    #         rightSum -= nums[i]
    #         differenceArray[i] = abs(rightSum - leftSum)
    #         leftSum += nums[i]

    #     return differenceArray
    
        """ comment on below code by Arslan Ahmad 
        Thank you for posting the code. The space complexity is right, but the time complexity is not O(n), it is O(n^2).

Look at what happens inside the loop. sum(nums[:i]) adds up i elements and sum(nums[i+1:]) adds up n - i - 1 elements, so a single iteration does about n units of work rather than constant work. The loop runs n times, so the total is about n times n. The two slices also build new lists on every iteration, so the code allocates memory it immediately throws away.

The constraint here is n <= 1000, so your version passes. It is still worth being precise about, because the linear version is the whole point of this question: keep leftSum and rightSum as two running numbers, subtract the current element from rightSum before you use it, then add it to leftSum after. Each index then costs constant work instead of a fresh scan of the array.

A useful habit for interviews: whenever a call like sum() or a slice appears inside a loop, its cost belongs in the analysis.
        """
    # O(n^2) TC 
        def findDifferenceArray(self, nums):
            n = len(nums)
            differenceArray = [0] * n
            # TODO: Write your code here
            for i in range(n):
                left_sum = sum(nums[:i])
                right_sum = sum(nums[i+1:])
                differenceArray[i] = abs(left_sum - right_sum)
            
            return differenceArray

# Testing the solution
solution = Solution()

example1 = [2, 5, 1, 6, 1]
example2 = [3, 3, 3]
example3 = [1, 2, 3, 4, 5]

print(solution.findDifferenceArray(example1))  # Output: [13, 6, 0, 7, 14]
print(solution.findDifferenceArray(example2))  # Output: [6, 0, 6]
print(solution.findDifferenceArray(example3))  # Output: [14, 11, 6, 1, 10]
