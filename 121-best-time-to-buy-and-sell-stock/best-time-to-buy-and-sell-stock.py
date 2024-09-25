class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l_idx = 0
        # for i in range(len(prices)):
        #     if prices[l_idx] > prices[i]:
        #         l_idx = i
        
        # if l_idx == len(prices)-1 : return 0

        # h_val = prices[l_idx]
        # h_idx = 0
        # for i in range(l_idx, len(prices)):
        #     if prices[i] > h_val and prices[i] > prices[l_idx] :
        #         h_idx = i
        #         h_val = prices[i]

        # return prices[h_idx] - prices[l_idx]

        buy_i = 0

        prof = 0        
        for i in range(1, len(prices)):
            if prices[buy_i] > prices[i]:
                buy_i = i
            
            prof = max([prices[i] - prices[buy_i], prof])
        
        return prof
