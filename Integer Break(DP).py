class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for i in range(n + 1)]
        result[0] = 0
        if n >= 1:
            result[1] = 0
        if n >= 2:
            result[2] = 1
        if n >= 3:
            result[3] = 2

        for i in range(4, n + 1):
            temp = []
            for j in range(1, i):
                temp.append(result[i - j] * j)
                temp.append((i - j) * j)
            print(temp)
            result[i] = max(temp)
        return result[n]