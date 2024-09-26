class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums) -1
        steps = far = end = 0
        if size == 0: return 0

        for i in range(size):
            far = max(far, i + nums[i])
            if i == end:
                steps+=1; end = far
            
            if end >= size: break
        return steps
            