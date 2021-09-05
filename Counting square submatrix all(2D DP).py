class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            if matrix[i][0] == 1:
                ans += 1
                dp[i][0] = 1
        for i in range(1, n):
            if matrix[0][i] == 1:
                ans += 1
                dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans += dp[i][j]
        return ans