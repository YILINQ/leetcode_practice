class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for i in range(num + 1)]
        for i in range(1, num+1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + 1
        return result