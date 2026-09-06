class Solution:
    def largestAltitude(self, gain):
        currentAltitude = 0  # To store the current altitude during iteration
        maxAltitude = 0  # To store the maximum altitude encountered

        # Iterate through the gain list, updating the current and max altitudes
        for i in gain:
            currentAltitude += i
            maxAltitude = max(currentAltitude, maxAltitude)

        return maxAltitude

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Expected: 1

    # Example 2
    print(solution.largestAltitude([4, -3, 2, -1, -2]))  # Expected: 4
    
    # Example 3
    print(solution.largestAltitude([2, 2, -3, -1, 2, 1, -5]))  # Expected: 4
