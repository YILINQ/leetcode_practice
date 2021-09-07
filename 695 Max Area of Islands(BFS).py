class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def checkUp(i, j):
            return 0 <= i <= m - 1 and 0 <= j - 1 <= n - 1 and not visited[i][j - 1] and grid[i][j - 1] == 1

        def checkDown(i, j):
            return 0 <= i <= m - 1 and 0 <= j + 1 <= n - 1 and not visited[i][j + 1] and grid[i][j + 1] == 1

        def checkLeft(i, j):
            return 0 <= i - 1 <= m - 1 and 0 <= j <= n - 1 and not visited[i - 1][j] and grid[i - 1][j] == 1

        def checkRight(i, j):
            return 0 <= i + 1 <= m - 1 and 0 <= j <= n - 1 and not visited[i + 1][j] and grid[i + 1][j] == 1

        ans = 0
        max_ans = -1
        queue = []
        for i in range(m):
            for j in range(n):
                ans = 0
                if grid[i][j] == 1 and not visited[i][j]:
                    queue.append((i, j))
                    visited[i][j] = True
                    ans = 1
                while queue != []:
                    current = queue.pop(0)
                    ii, jj = current[0], current[1]
                    # check 4 directions
                    if checkUp(ii, jj):
                        queue.append((ii, jj - 1))
                        ans += 1
                        visited[ii][jj - 1] = True
                    if checkDown(ii, jj):
                        queue.append((ii, jj + 1))
                        ans += 1
                        visited[ii][jj + 1] = True
                    if checkLeft(ii, jj):
                        queue.append((ii - 1, jj))
                        ans += 1
                        visited[ii - 1][jj] = True
                    if checkRight(ii, jj):
                        queue.append((ii + 1, jj))
                        ans += 1
                        visited[ii + 1][jj] = True
                if ans >= max_ans:
                    max_ans = ans

        return max_ans