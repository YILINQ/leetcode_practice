# 给定一个只包含大小写字母的字符串（大小写敏感），
# 若相邻两个元素相等则消除，直到最后字符串消除不了了，
# 输出消消乐后字符串的长度，若遇到非大小写字母以外的字符，则输出0
def stack_cancel(string):
    stack = [string[0]]
    for i in range(1, len(string)):
        flag = True
        while stack != []:
            flag = False
            current = stack.pop()
            if current == string[i]:
                # cancelled
                break
            else:
                stack.append(current)
                stack.append(string[i])
                break
        if flag:
            stack.append(string[i])
    return len(stack)



if __name__ == "__main__":

    s = input()
    if not all([char.isalpha() for char in s]):
        print(0)
    if len(s) == 0:
        print(0)
    if len(s) == 1:
        print(1)
    if len(s) > 1:
        print(stack_cancel(s))