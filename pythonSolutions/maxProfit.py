'''Max Profit Problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

def maxProfit(self, prices) -> int:
    # set minimum price to be the first price
    min_price = prices[0]
    max_profit = 0

    # ignoring the first price, as it is already set, for every other price in prices
    for price in prices[1:]:
        # calculate the difference between the price and the minimum price
        diff = price - min_price
        # determine max profit as either our current max profit, or the difference
        max_profit = max(max_profit, diff)
        # determine the minimum price as either the minimum price, or the price we currently have
        min_price = min(min_price, price)

    # return max profit
    return max_profit