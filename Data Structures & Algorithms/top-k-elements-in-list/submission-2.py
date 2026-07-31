class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total = {}  # num : times_it_occurred
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            total[num] = total.get(num, 0) + 1

        for key, value in total.items():
            freq[value].append(key)

        result = []
        for idx in range(len(freq) - 1, -1, -1):
            if freq[idx]:
                for el in freq[idx]:
                    result.append(el)
        
        print(result)
        return result[:k]
