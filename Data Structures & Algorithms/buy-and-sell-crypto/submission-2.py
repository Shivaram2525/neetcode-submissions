class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        prof=0
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            prof=max(prof,prices[i]-mini)
        return prof