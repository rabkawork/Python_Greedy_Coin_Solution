#!/usr/bin/env python3
import sys

print("Mencari solusi maksimal penukaran koin dengan algoritma Greedy : ")

def fit(n, coin, needle):
    return (n+coin) <= needle

def greedy(coins, needle, MAXORMIN):
    solution = []

    if(MAXORMIN):
        coins.sort(reverse=True)
    
    #print(coins)
    while (sum(solution) != needle):
        for coin in coins:
            total = sum(solution)
            if fit(total,coin, needle):
                solution.append(coin)
    return solution
    


if __name__ == '__main__':
    money = 2200
    coins = [100,200,500,1000,2000]

    print("Koin : {0}".format(coins))
    print("Uang yang ditukar : {0}".format(money))
    print("Solusi Minimal : {0}".format(greedy(coins, money, False)))
    print("Solusi Maksimal : {0}".format(greedy(coins, money, True)))