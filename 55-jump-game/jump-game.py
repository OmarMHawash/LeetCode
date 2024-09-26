class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0; size = len(nums)
        can_reach = 0
        if size == 1: return True

        while(i < size-1):
            if can_reach < i: return False
            
            can_reach = max(can_reach, i + nums[i])
            if can_reach >= size - 1:
                return True
            
            i += 1
        return False