

#problem no 9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        if n >= 0:
            sign = 1
        else:
            sign = -1

        n = abs(n)
        reverse = int(str(n)[::-1])
        reverse = reverse * sign
       
        if n == reverse:
            return True
        else:
            return False
        