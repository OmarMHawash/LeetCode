class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        MAX = 0
        SET = set(nums)

        for val in SET:
            if (val-1) not in SET:
                n = 1
                while (val+n) in SET:
                    n += 1
                MAX = max(MAX, n)
        
        return MAX