class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search: lo, hi = 0, len(nums) - 1

        # while nums[lo] <= nums[hi]
        # mid = (lo + hi) // 2
        # if nums[mid] == target: return mid

        # if nums[mid] < nums[hi]: we are in sorted part
        ## if target inside mid-hi: set lo = mid
        ## else set hi = mid
        # else nums[mid] > nums[hi]: lowest num is to right
        ## if target inside nums[lo]-nums[mid] : set mid = hi
        ## else set mid = lo

        ## outside while, return -1

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[hi]:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1
        # lo, hi, mid = 0, 1, 0
        # nums[mid] = 1
        # nums[hi] = 3

        # [1, 3], target = 2
