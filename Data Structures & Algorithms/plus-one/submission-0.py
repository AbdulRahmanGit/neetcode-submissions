class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for digit in digits:
            num += str(digit)

        int_num = int(num) + 1
        int_list = [i for i in str(int_num)]
        return int_list