class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i, cover = 0, 0
        # cover the the furthest I can get, iterate all step in 
        # the cover
        while i <= cover:
            cover = max(i+nums[i], cover)
            i += 1
            if cover >= len(nums)-1:
                return True 
        return False