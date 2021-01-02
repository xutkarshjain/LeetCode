'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        loc=-1
        for i in nums:
            if i!= val:
                nums[loc+1]=i
                loc+=1
        return loc+1
