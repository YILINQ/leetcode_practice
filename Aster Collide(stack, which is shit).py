class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for item in asteroids:
            if item > 0:
                result.append(item)
            else:
                flag = True

                if result == [] or result[-1] < 0:
                    result.append(item)
                else:
                    while result and result[-1] > 0:
                        last = result.pop()
                        if abs(last) < abs(item):
                            pass
                        elif abs(last) == abs(item):
                            flag = False
                            break
                        else:
                            result.append(last)
                            flag = False
                            break
                    if flag:
                        result.append(item)

        return result