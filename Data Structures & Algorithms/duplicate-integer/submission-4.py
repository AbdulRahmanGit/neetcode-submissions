class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                #[1,2,3,3]
                if nums[i] == nums[j]:
                    return True
        return False
