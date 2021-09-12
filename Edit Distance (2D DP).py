class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        if len(word1) == len(word2) == 1:
            if word1 == word2:
                return 0
            else:
                return 1
        f = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        for i in range(len(word2) + 1):
            f[i][0] = i

        for i in range(len(word1) + 1):
            f[0][i] = i

        for i in range(1, len(f)):
            for j in range(1, len(f[0])):
                if word2[i - 1] == word1[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        for row in f:
            print(row)
        return f[-1][-1]

