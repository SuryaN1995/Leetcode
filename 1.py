from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()
        for index, num in enumerate(nums):
            diff = target - num
            if num in data:
                return [index, data[num]]
            else:
                data[diff] = index