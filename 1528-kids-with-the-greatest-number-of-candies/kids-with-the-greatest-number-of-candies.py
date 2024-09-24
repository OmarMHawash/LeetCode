class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for c in candies:
            new = c + extraCandies
            if new >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
