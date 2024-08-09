def find_coins_greedy(n: int, nominals: list) -> dict:
    res = {}
    for el in reversed(nominals):
        if el <= n and n > 0:
            res[el] = n // el
            n = n % el

    return res


def find_min_coins(n: int, nominals: list) -> dict:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    used_coins = [0] * (n + 1)

    for i in range(1, n + 1):
        for coin in nominals:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    used_coins.insert(i, coin)

    if dp[n] == float('inf'):
        return {}

    result = {}
    while n > 0:
        coin = used_coins[n]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        n -= coin

    return result


# NOMINALS = (1, 2, 5, 10, 25, 50)
NOMINALS = (1, 3, 4, 6)
N = 8

print(f"Видаю здачу у розмірі {N} коп.")
print(f"Отримано жадібним алгоритмом - {find_coins_greedy(N, NOMINALS)}")
print(f"Отримано за допомогою ДП     - {find_min_coins(N, NOMINALS)}")
