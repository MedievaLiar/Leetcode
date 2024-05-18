class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # make n, m last pointers
        n -= 1
        m -= 1
        # pointernums1 is a last pointer for nums1
        pointerNums1 = n + m + 1

        while n > -1 or m > -1:

            if n == -1:
                nums1[pointerNums1] = nums1[m]
                m -= 1
            elif m == -1:
                nums1[pointerNums1] = nums2[n]
                n -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[pointerNums1] = nums1[m]
                    m -= 1
                else:
                    nums1[pointerNums1] = nums2[n]
                    n -= 1
            pointerNums1 -= 1
