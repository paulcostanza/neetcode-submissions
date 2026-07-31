class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, curr = 0, 0

        char_set = set()

        left, right = 0, 0

        for right in range(len(s)):
            if s[right] not in char_set:
                char_set.add(s[right])
                curr += 1
            else:
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                    curr -= 1
                left += 1
                # curr -= 1

            if curr > longest:
                longest = curr

        return longest