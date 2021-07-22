class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        max_len = 0
        start_index = 0
        
        for i in range(len(s)):
            
            if s[i] in last_index:
                start_index = max(start_index, last_index[s[i]]+1)
            
            max_len = max(max_len, i-start_index+1)
            
            last_index[s[i]] = i
            
        return max_len
