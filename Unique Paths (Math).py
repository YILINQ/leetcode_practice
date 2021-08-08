import operator as op
import math

class Solution:
    def ncr(self, n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, xrange(n, n-r, -1), 1)
        denom = reduce(op.mul, xrange(1, r+1), 1)
        return numer//denom
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = math.factorial
        return f(m+n-2) // (f(n-1) * f(m-1))