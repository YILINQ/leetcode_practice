class Solution:
    def rob(self, nums) -> int:
        opt1 = []
        opt2 = []

        without_head = nums[1:]
        without_tail = nums[:-1]

        if (len(nums) == 1):
            return nums[0]

        if not without_head or not without_tail:
            return 0

        opt1 = [without_head[0]]
        opt2 = [without_tail[0]]
        temp1 = 0
        temp2 = 0
        if len(without_head) >= 2:
            opt1.append(max(without_head[0], without_head[1]))
        else:
            temp1 = opt1[0]
        if len(without_tail) >= 2:
            opt2.append(max(without_tail[0], without_tail[1]))
        else:
            temp2 = opt2[0]

        for i in range(2, len(without_head)):
            x1 = max(opt1[i - 1], opt1[i - 2] + without_head[i])
            opt1.append(x1)

        for i in range(2, len(without_tail)):
            x2 = max(opt2[i - 1], opt2[i - 2] + without_tail[i])
            opt2.append(x2)

        return max(temp1, temp2, opt1[-1], opt2[-1])