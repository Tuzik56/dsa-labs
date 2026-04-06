def greedy(coins, money):
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while money - coin >= 0:
            result.append(coin)
            money -= coin

    return result


def dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [-1] * (amount + 1)

    for part in range(1, amount + 1):
        for coin in coins:
            if part - coin >= 0 and dp[part - coin] + 1 < dp[part]:
                dp[part] = dp[part - coin] + 1  # минимальное кол-во монет
                prev[part] = coin  # последняя монета

    result = []

    while amount > 0:
        coin = prev[amount]
        result.append(coin)
        amount -= coin

    return result


coins = [[1, 5, 10, 25, 50, 100], [1, 4, 6, 9]]
amounts = [23, 37, 58, 74, 99, 123]

for amount in amounts:
    print(f"___ Amount: {amount} ___")

    for coin in coins:
        print(f"Coins: {coin}")
        print(f"Greedy: {greedy(coin, amount)}")
        print(f"DP: {dp(coin, amount)}")
        print()

    print()