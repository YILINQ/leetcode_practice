class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = []
        for i in range (n+1):
            f.append(0)
        f[0], f[1] = 1, 1
        for i in range(2, n+1):
            ans = 0
            for j in range(i+1):
                ans += f[j] * f[i-j-1]
            f[i] = ans
        for i in range(n):
            print (f[i])
        return f[n]