class Solution(object):
    def countSquares(self, matrix):
        answer = 0
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if (r == 0 or c == 0):
                    if matrix[r][c] == 1:
                        answer += 1
                elif matrix[r][c] == 1:
                    matrix[r][c] = min(matrix[r-1][c], min(matrix[r][c-1], matrix[r-1][c-1])) + 1
                    #увеличиваем квадрат с помощью нахождения минимума из диагонального, левого и верхнего соседа
                    answer += matrix[r][c]
        return answer
#Сложность функции O(n*m)

