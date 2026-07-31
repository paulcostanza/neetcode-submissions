class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = {}
        letters_t = {}

        for idx in range(len(s)):
            if s[idx] in letters_s:
                letters_s[s[idx]] += 1
            else:
                letters_s[s[idx]] = 1

            if t[idx] in letters_t:
                letters_t[t[idx]] += 1
            else:
                letters_t[t[idx]] = 1

        return letters_s == letters_t