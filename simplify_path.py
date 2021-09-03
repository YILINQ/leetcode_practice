class Solution:
    def simplifyPath(self, path: str) -> str:
        levels = path.split('/')
        stack = []
        print(levels)
        for level in levels:
            if level != '':
                flag = True
                while stack != [] and level == '..' or level == '.':
                    current = stack.pop()
                    if level == "..":
                        flag = False
                        break
                    elif level == '.':
                        stack.append(current)
                        flag = False
                        break
                        # level = directory or level = .
                if flag:
                    stack.append(level)
        result = ('/' + '/'.join(stack))
        if result[-1] == '/':
            result = result[:-1]
        return result


