# 给定一个n*n的只包含0和1的二维矩阵，请你计算出该矩阵的最大值。
# 计算方式为将每一行的元素组成二进制数的十进制数相加，每一行元素可以进行左移右移（实质就是求出每行的最大值相加
# 比如说10001向左移一位就是00011

def binary_to_decimal(string):
    n = len(string)
    result = 0
    for i in range(n):
        result += int(string[i]) * (2 ** (n - i -1))
    return result
def convert_row_max(row):
    # row is a string
    max_ = 0
    for i in range(len(row)):
        new_string = row[i:] + row[:i]
        if  binary_to_decimal(new_string) > max_:
            max_ = binary_to_decimal(new_string)
    return max_

if __name__ == "__main__":
    n = input()
    total = 0
    try:
        n = int(n)
        i = 0
        while i < n:
            row = input()
            row = row.split(',')
            assert len(row) == n
            total += convert_row_max(''.join(row))

            i += 1

    except:
        print("wrong input")

    print(total)