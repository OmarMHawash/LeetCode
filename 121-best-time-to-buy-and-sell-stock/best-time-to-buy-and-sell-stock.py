class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_i = 0
        prof = 0

        for i in range(1, len(prices)):
            if prices[buy_i] > prices[i]:
                buy_i = i
            prof = max(prices[i] - prices[buy_i], prof)
        
        return prof