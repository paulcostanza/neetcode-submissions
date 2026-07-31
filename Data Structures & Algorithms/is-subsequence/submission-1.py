class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through t
        # if t's char matches s's char then I iterate through s
        # if no more chars in s, return True
        # if I finish iterating through t, return False

        if s == "":
            return True

        idx = 0

        for char in t:
            if char == s[idx]:
                idx += 1
                if idx == len(s):
                    return True

        return False


        
        