class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        n = len(needle)
        if haystack == needle:
            return 0
        for i in range(l):
            if haystack[i:i+n] == needle:
                return i
        return -1