class Solution:
    def runningSum(self, nums):
        # Check if the array is None or has no elements and return an empty list if true
        if nums is None or len(nums) == 0:
            return []
        
        # Initialize a list to store the running sum
        result = [0] * len(nums)
        result[0] = nums[0]
        
        # Loop through the list starting from index 1, adding the previous sum to the current element
        for i in range(1, len(nums)):
            result[i] = result[i - 1] + nums[i]
        
        # Return the list containing the running sum
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    testInputs = [
        [2, 3, 5, 1, 6],
        [1, 1, 1, 1, 1],
        [-1, 2, -3, 4, -5]
    ]

    for input_arr in testInputs:
        output = solution.runningSum(input_arr)
        
        # Print the output list
        print(" ".join(map(str, output)))
