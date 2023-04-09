class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1: #обходим ячейку c препятствием
                    dp[row][col] = 0
                    continue
                if row > 0:
                    dp[row][col] += dp[row - 1][col]
                if col > 0:
                    dp[row][col] += dp[row][col - 1]
        return dp[-1][-1]

# Сложность функции O((n+1)*(m+1))