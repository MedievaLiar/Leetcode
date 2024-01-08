#beats 89%

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        zeros = 0
        for num in range(N):
            if nums[i] == 0:
                zeros += 1
            else:
                nums.append(nums[i])
        del nums[:N]
        nums += ([0] * zeros)
