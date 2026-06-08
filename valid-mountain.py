from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) :
        if len(arr) < 3 :
            return False
        i = 1 
        while(i < len(arr) and arr[i] > arr[i-1]):
            i+=1
        if(i==1 or i == len(arr)):
            return False
             # edge case what if the array has only one element ? And what is the array is sorted and has only A[i] > A[i-1] till the end 
        while(i < len(arr) and arr[i] < arr[i-1]):
            i+=1

        if( i == len(arr)): 
            return True     
        
        
s = Solution()
print(s.validMountainArray([0, 1, 0]))
