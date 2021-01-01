'''

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and
returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.


Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.

'''





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        last=nums[0]-1
        loc=-1
        for i in nums:
            if i!=last:
                loc+=1
                nums[loc]=i
                last=i
        return loc+1
                
