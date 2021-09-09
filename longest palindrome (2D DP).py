class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        if len(s) == 1:
            return s
        f = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1):
            f[i][i] = 1
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2
        f[len(s) - 1][len(s) - 1] = 1

        # s[i : j] is a palindrome if and only if:
        # f[i][j] = True

        max_len = 0
        result = ""
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if s[i] == s[j]:
                    f[i][j] = max(f[i + 1][j - 1] + 2, f[i][j])

                # if f[i][j] > max_len:
                #     max_len = f[i][j]
                #     result = s[i:j+1]
        return f[0][len(s) - 1]