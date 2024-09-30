class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Map = {}
        for i in range(len(nums)):
            if nums[i] in Map.keys() and abs(Map[nums[i]] - i) <=k:
                return True
            else:
                Map[nums[i]] = i
        return False