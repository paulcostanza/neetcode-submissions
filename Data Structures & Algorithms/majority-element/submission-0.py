class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}

        current, occurrences = 0, 0

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

            if num_dict[num] > occurrences:
                current = num
                occurrences = num_dict[num]
            
            if occurrences > len(nums) // 2:
                return current

