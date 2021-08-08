class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        start = coordinates[0]
        end = coordinates[1]
        cosTheta = 0
        vec1 = [start[0] - end[0], start[1] - end[1]]
        for item in coordinates[2:]:
            newEnd = item
            vec2 = [start[0] - newEnd[0], start[1] - newEnd[1]]

            # compute cosTheta
            cosTheta = vec1[0] * vec2[1] - vec1[1] * vec2[0]
            # compute cosTheta
            if cosTheta != 0:
                return False
        return True