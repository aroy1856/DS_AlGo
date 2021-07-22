class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0) ^ (divisor < 0):
            s = -1
        else:
            s = 1
        m = 2**31
        dividend = abs(dividend)
        divisor = abs(divisor)
        temp = 0
        q = 0
        
        #check from the highest bbit value according to 2's power and construct the quotent
        for i in range(31,-1,-1):
            if ((temp + (divisor<<i)) <= dividend):
                temp += (divisor<<i)
                q |= 1<<i
        r = q * s
        #overflow detection
        if (r < (m*-1)) or (r > m-1):
            return m-1
        return r
                
        