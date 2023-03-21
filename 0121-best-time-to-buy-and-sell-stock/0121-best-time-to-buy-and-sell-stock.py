class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer?
        #move left pointer if price[left] > price[right]
        #move right pointer til end of list

        pl = 0
        pr = 1
        maxp = 0
        while(pr < len(prices)):
            profit = prices[pr] - prices[pl]
            if profit <= 0:
                pl = pr
            else:
                maxp = max(maxp, profit)
            pr = pr + 1

        return maxp


        