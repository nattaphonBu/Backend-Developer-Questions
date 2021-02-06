## total_profit = (sell_price - cost_price) * inventory
def calculete_total_profit(profit):
    total_profit = (profit['sell_price'] - profit['cost_price']) \
        * profit['inventory']
    ## used fuction round to rounding total_profit to integer
    print(round(total_profit))

profit = ({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
})
profit_2 = ({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
})
profit_3 = ({
    "cost_price": 550.00,
    "sell_price": 225.89,
    "inventory": 100
})
profit_4 = ({
    "cost_price": 550.00,
    "sell_price": 225.89,
    "inventory": 0
})
calculete_total_profit(profit)
## ouput should be -> 14796
calculete_total_profit(profit_2)
## ouput should be -> 32411
calculete_total_profit(profit_3)
## ouput should be -> -32411
calculete_total_profit(profit_4)
## ouput should be -> 0
