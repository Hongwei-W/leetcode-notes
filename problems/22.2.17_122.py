class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         perchase = False 
#         total = 0
#         last_day = 0
#         for i in range(0, len(prices)):
#             if i == len(prices)-1 :
#                 if perchase:
#                     total += prices[i] - prices[last_day]
#                     return total
            
#             elif prices[i+1] > prices[i]:
#                 if not perchase:
#                     perchase = True 
#                     last_day = i
#                 # else:
#                 #     if i+1 == len(prices)-1:
#                 #         total += prices[i+1] - prices[last_day]
#                 #         return total
#             else:
#                 if perchase:
#                     total += prices[i] - prices[last_day]
#                     perchase = False
#         return total
       
        # buy and sell 2 days after == repeat "buy and sell 1 days after" 2 times
        total = 0
        for i in range(1, len(prices)):
            total += max(prices[i]- prices[i-1], 0)
        return total 