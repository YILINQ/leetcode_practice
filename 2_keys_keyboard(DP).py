class Solution:
    def minSteps(self, n: int) -> int:
        # recurrence: min(minSteps(n // i) + i for i in range(1, n) if n % i == 0

        # slow and memory consumed.
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n == 3:
            return 3

        minSteps_array = []

        # init empty array
        for i in range(n + 1):
            minSteps_array.append(0)

        # init base cases
        minSteps_array[1] = 0
        minSteps_array[2] = 2
        minSteps_array[3] = 3

        for i in range(4, n + 1):
            minSteps_array[i] = min([minSteps_array[j] + i // j for j in range(1, i) if i % j == 0])
        print(minSteps_array)
        return minSteps_array[-1]