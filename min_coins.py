def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

print(find_min_coins(199844))  # {50: 3996, 25: 1, 10: 1, 5: 1, 2: 2}