class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0

        if len(grid) == 0:
            return 0

        for i in range(len(grid)): #для i по количеству элементов grid
            for j in range(len(grid[i])): #для j по количеству элементов r
                if grid[i][j] == 1: #если клетка = 1
                    perimeter += 4 #периметр увеличиваем на 4
                    if i > 0 and grid[i - 1][j] == 1: #верхняя клетка
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1: #левая клетка
                        perimeter -= 2
        return perimeter

#Сложность O(n)