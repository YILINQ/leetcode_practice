class Solution:
    def superPow(self, a, b, c=1337):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        str = ''
        x = []
        for item in b:
            x.append(repr(item))
        new_b = int(str.join(x))
        result = 1
        while(new_b != 0):
            if(new_b & 1):
                result = (result * a)% c
            a = (a * a) % c
            new_b = new_b >> 1
        return result