class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Let A[key, remain] to be the current state, either true or false
        #
        # if A[word, string=word] then return True
        # if A[word, len(string) < len(word)] then return False
        # else:
        #     A[word, string] = A[word, string - word from head] or A[word, string - word from tail]
        A = [False for _ in range(len(s) + 1)]
        A[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and A[j]:
                    A[i] = True
        return A[-1]