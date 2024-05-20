from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_pos = bisect_left(nums, target)
        right_pos = bisect_right(nums, target) - 1
        try:
            l = nums[left_pos]  
        except IndexError: # In case binsearch didn't find the element and returned the latest index
            return[-1, -1]
        else:
            if l != target: # In case binsearch didn't find the element and returned the index of closes element
                return [-1, -1]
            return [left_pos, right_pos]        
