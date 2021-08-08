class Solution:

    # all test cases passed
    # but time limit exceed, need to be optimized
    def maxEnvelopes(self, envelopes) -> int:
        arr = envelopes.copy()
        arr.sort(key=lambda s: (s[0], s[1]))
        f = []
        for i in range(len(arr)):
            f.append(1)
        for i in range(len(arr)):
            max_num = -1
            for j in range(i):
                if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1

        return max(f)