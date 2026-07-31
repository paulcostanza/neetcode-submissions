class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, num in enumerate(nums):
            difference = target - num
            if difference in nums_map:
                return [nums_map[difference], idx]
            nums_map[num] = idx