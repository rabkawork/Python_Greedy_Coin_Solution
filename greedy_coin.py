#!/usr/bin/env python3
import random
print("Mencari solusi minimum penukaran koin dengan algoritma Greedy : ")

def greedy(coins, needle):
    solution = []
    
    # sort urutan data dari terkecil ke terbesar
    coins.sort(reverse=True)
    
    for coin in coins:
        while (needle >= coin): 
            needle -= coin
            solution.append(coin)

    if sum(solution) != needle:
        solution = "Solusi tidak ditemukan"

    return solution

if __name__ == '__main__':
    money = 1050
    coins = [100,200,500,1000]

    print("Koin : {0}".format(coins))
    print("Uang yang ditukar : {0}".format(money))
    print("Solusi Greedy : {0}".format(greedy(coins, money)))