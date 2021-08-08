class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        l = obstacleGrid
        width = len(l[0])
        height = len(l)

        dp = []
        row = [0 for _ in range(width)]
        for i in range(height):
            dp.append(row.copy())

        # first col
        for row in range(height):
            if l[row][0] == 0:
                dp[row][0] = 1
            else:
                for j in range(row, height):
                    dp[row][0] = 0
                break

        # first row
        for i in range(width):
            if l[0][i] == 0:
                dp[0][i] = 1
            else:
                for j in range(i, width):
                    dp[0][j] = 0
                break
        print(dp)

        # dp part
        for j in range(1, width):
            for i in range(1, height):
                if l[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]