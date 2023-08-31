class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        nums.append(math.inf)

        l = 0

        for r in range(1, len(nums)):
            if nums[l] + (r - l) != nums[r]:
                if r - l == 1:
                    res.append(str(nums[l]))
                else:
                    _range = f"{nums[l]}->{nums[r - 1]}"
                    res.append(_range)
                l = r
        return res
