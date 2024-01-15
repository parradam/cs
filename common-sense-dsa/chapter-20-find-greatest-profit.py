def find_greatest_profit(prices):
    lowest_price = prices[0]
    highest_price = prices[0]
    profit = 0

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        elif price > highest_price:
            highest_price = price
            profit = highest_price - lowest_price

    return profit


# The greatest profit with one buy and one sell
# transaction would be by buying at $5 and
# selling at $11 for a profit of $6
prices = [10, 7, 5, 11, 2, 6]

print(find_greatest_profit(prices))
