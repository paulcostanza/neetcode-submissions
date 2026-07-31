class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checking = {}

        for num in nums:
            if num in checking:
                return True
            else:
                checking[num] = 1

        return False