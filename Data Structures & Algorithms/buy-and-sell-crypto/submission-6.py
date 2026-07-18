class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = prices[0]
        for price in prices:
            curr = min(curr, price)
            profit = max(profit, price - curr)
        return profit