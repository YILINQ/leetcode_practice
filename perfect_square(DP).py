class Solution:

    #  N^2 solution
    def numSquares(self, n: int) -> int:
        lookup = [i * i for i in range(1, n+1)]
        if n in lookup:
            return 1

        f = [0, 1, 2, 3, 1]
        if n <= 4:
            return f[n]
        ans = 100
        for i in range(5, n+1):
            if i in lookup:
                f.append(1)
            else:
                ans = 100
                for j in range(1, i):
                    if f[i - j] + f[j] < ans:
                        ans = f[i - j] + f[j]
                f.append(ans)
        return f[-1]