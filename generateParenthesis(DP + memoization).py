class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 1, ()
        # n = 2, (()), ()()
        # n = 3, ((())),
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        self.lst = ["(())", "()()"]
        for i in range(n - 2):
            self.helper()
        return self.lst

    def helper(self):
        # n >= 2
        temp = []
        for string in self.lst:
            for i in range(len(string)):
                string_list = list(string)
                string_list.insert(i, "()")
                temp.append(''.join(string_list))

        self.lst = list(set(temp))