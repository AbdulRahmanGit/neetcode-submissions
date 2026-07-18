class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2  = nums[slow2]
            if slow == slow2:
                return slow       