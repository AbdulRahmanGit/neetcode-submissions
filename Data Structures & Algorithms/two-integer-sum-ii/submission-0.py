class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)  - 1
        while l < r:
            mid = numbers[l] + numbers[r]
            if target == mid:
                return [l + 1, r + 1]
            elif target > mid:
                l += 1
            elif target < mid:
                r -= 1
        return [0,0]