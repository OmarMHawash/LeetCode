class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        M = {}
        for i in range(len(nums)):
            if nums[i] in M.keys() and abs(M[nums[i]] - i) <=k:
                return True
            else:
                M[nums[i]] = i
        return False