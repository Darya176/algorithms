class Solution(object):
    def getDescentPeriods(self, prices):
        p = [1] * len(prices)  # создаем массив
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:  # сравниваем массив
                p[i] += p[i - 1]
        return sum(p)

#Сложность функции O(n)