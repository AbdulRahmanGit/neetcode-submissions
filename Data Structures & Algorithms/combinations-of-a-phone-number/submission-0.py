class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {  '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def backtrack(comb, next_digit):
            if len(next_digit) == 0:
                res.append(comb) 
            else:
                for val in mapping[next_digit[0]]:
                    backtrack(comb + val, next_digit[1:])
        if digits:
            backtrack('', digits)
        return res