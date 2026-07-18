class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        while x > 0:
            res = (res * 10) + x % 10
            x //= 10
        if res > 2 ** 31 - 1:
            return 0
        return res * -1 if is_negative else res
        '''
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        if (res < -2 ** 31)  or (res > 2 ** 31 - 1):
            return 0
        return res
        '''
        