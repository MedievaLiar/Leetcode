from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a = {0 : 1}
        
        subarraySumEqualK = 0
        prefixsum = 0
        for num in nums:
            prefixsum += num
            if a.get(prefixsum - k) != None:
                subarraySumEqualK += a[prefixsum - k]
            
            if a.get(prefixsum) == None:
                a[prefixsum] = 0
            
            a[prefixsum] += 1

        return subarraySumEqualK
