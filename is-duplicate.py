class Solution:
  def containsDuplicate(self, nums):
    unique_set = set() # Use set to store unique elements
    
    for x in nums:
      if x in unique_set: # If the set already contains the current element, return True
        return True
      unique_set.add(x) # Add the current element to the set

    return False # Return False if no duplicates found

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.containsDuplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.containsDuplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.containsDuplicate(nums3)) # Expected output: False

  nums4 = [3, 2, 6, -1, 2, 1]
  print(sol.containsDuplicate(nums4)) # Expected output: True
