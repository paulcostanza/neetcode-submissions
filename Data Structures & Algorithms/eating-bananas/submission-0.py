import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = -1

        while lo <= hi:
            k = (lo + hi) // 2 # mid
            total_hours = 0

            for p in piles:
                # most = max(piles)
                total_hours += math.ceil(p / k)

            if total_hours <= h:
                result = k
                hi = k - 1
            else: # does not work, is too high
                lo = k + 1

        return result
            