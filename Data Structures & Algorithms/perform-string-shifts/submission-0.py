class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # loop shift
        # if sh[0] == 0: sh[1] * -1
        # else: sh[1] += 1
        
        
        for sh in shift:
            if sh[0] == 1:
                s = s[sh[1] * -1 : ] + s[: sh[1] * -1]
            elif sh[0] == 0:
                s = s[sh[1] :] + s[: sh[1]]

        return s
        # [1,1],[0,2],[1,3]
        # abcdefg