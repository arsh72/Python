class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = float(inf)
        profit=0
        for price in prices:
            buyprice=min(price,buyprice)
            if (price-buyprice>0):
                profit=max(profit,price-buyprice)
        return profit
        
        