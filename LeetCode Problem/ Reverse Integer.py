


#problem NO:7

class Solution:
    def reverse(self, x: int) -> int:
        Int_max,Int_min = 2 ** 31 - 1, -2 **31
        if x > 0 :
            sign = 1
        else:
            sign = -1
        
        x = abs(x)

        n = x
        Reverse_count = 0
        while x > 0 :

            last_digit = x % 10
            Reverse_count = Reverse_count * 10 + last_digit
            x = x // 10
        Reverse_count = Reverse_count * sign
        if Reverse_count > Int_max or Reverse_count < Int_min:
            return 0


        return Reverse_count

a = Solution()
print(a.reverse(-1230))

