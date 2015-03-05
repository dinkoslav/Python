def calculate_coins(sum):
    coins = { 1: 0, 
              2: 0, 
              100: 0, 
              5: 0, 
              10: 0, 
              50: 0, 
              20: 0
            }
    sum = sum * 100
    coin_types = [100,50,20,10,5,2,1]
    for coin_type in coin_types:
        while sum >= coin_type:
            sum = sum - coin_type
            coins[coin_type] = coins[coin_type] + 1

    return coins

first_test = calculate_coins(0.53)
second_test = calculate_coins(8.94)

print(first_test)
print(second_test)
