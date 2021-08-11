from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        a = ['0', '1']
        
        for i in range(n-1):
            a = a + a[::-1]
            
            l = len(a)//2
            
            for j in range(l):
                a[j] = '0' + a[j]
            for k in range(l, len(a)):
                a[k] = '1' + a[k]
                
        for i in range(len(a)):
            a[i] = int(a[i], 2)
        
        return a