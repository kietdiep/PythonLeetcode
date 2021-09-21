from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # nums = [1,2,3,4,5,6,7], k = 3
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]



nums = [1,2,3,4,5,6,7]

print(nums[-2:])
print(nums[:-2])
print(nums[-2:] + nums[:-2])
k = 3 % len(nums)
print(k)