import timeit


def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
        num_coins = amount // coin
        if num_coins > 0:
            result[coin] = num_coins
            amount -= num_coins * coin

    return result


def find_min_coins(sum, coins):
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    coins_count = {}
    current_sum = sum

    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    return {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}


amount = 113
coins = [50, 25, 10, 5, 2, 1]
functions = [find_coins_greedy, find_min_coins]

for fun in functions:
    time = timeit.timeit(lambda: fun(amount, coins), number=100)
    print("Result for {}: {}".format(fun.__name__, fun(amount, coins)))
    print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))
