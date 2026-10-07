class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # 2 pointers to keep track of char in s and char in t
        i, j = 0, 0

        if s == "":
            return True

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

