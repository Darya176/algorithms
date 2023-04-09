class Solution(object):
    def maxProfit(self, prices):
        max_p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: # сравниваем цену с предыдущей
                max_p += prices[i] - prices[i-1]                 #прибыль + разность
        return max_p        # возвращается максимальная прибыль

#Сложность функции O(n*m)