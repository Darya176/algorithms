class Solution(object):
    def getMaximumGenerated(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = [0]*(n+1)
        a[1] = 1
        for i in range(2, n+1):
            if i%2 == 0:
                a[i] = a[i//2]
            else:
                a[i] = a[i//2] + a[i//2 + 1]
        return max(a) #возвращаем максимальный элемент списка
#Сложность функции O(n)