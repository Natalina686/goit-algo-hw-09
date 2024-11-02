import time

# Номінали монети
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result

def find_min_coins(amount):
    # Ініціалізуємо масив для зберігання мінімальної кількості монет
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для нульової суми потрібно нуль монет

    # Масив для зберігання вибраних монет
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin not in result:
            result[coin] = 0
        result[coin] += 1
        amount -= coin

    return result

# Тестування та вимірювання часу виконання
def test_algorithms(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    min_coins_result = find_min_coins(amount)
    min_coins_time = time.time() - start_time

    print(f"Greedy Result: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming Result: {min_coins_result}, Time: {min_coins_time:.6f} seconds")

# Приклад
amount_to_return = 113
test_algorithms(amount_to_return)