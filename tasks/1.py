# Beats 90% O(N)
from typing import List
class Solution:
    def find_Two_Same_Indexes(nums, num):
        first, second = -1, -1
        for i in range(len(nums)):
            if nums[i] == num:
                if first == -1:
                    first = i
                else:
                    second = i
                    break
        
        return first, second
    
    def generate_dict(nums):
        a = dict()
        for num in nums:
            if a.get(num) == None:
                a[num] = 0
            a[num] += 1
        return a
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = Solution.generate_dict(nums)
        
        for num in nums:
            if (target - num) == num:
                if a[num] >= 2:
                    first, second = Solution.find_Two_Same_Indexes(nums, num)
                    break
            
            elif a.get((target - num)) != None:
                first = nums.index(num)
                second = nums.index(target - num)
                break
        
        return [first, second]
            
