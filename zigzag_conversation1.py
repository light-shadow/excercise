# coding: utf-8
# 根据一个java程序改写的python程序，算法复杂度较高，共有四重循环


def zigzag(s, rows):
    if rows == 1 or len(s) == 0:
        return s
    length = len(s)
    k = 0
    j = 0
    i = 1
    interval = rows * 2 - 2
    res = ['' for b in range(len(s))]  # 创了一个长度为字符串长度s的空list
    # 第一行字符串
    while(j < len(s)):
        res[k] = s[j]
        k += 1
        j += interval
    # 中间行字符串
    while(i < rows - 1):
        inter = i * 2
        j = i
        while(j < length):
            res[k] = s[j]
            k += 1
            j += inter
            inter = interval - inter
        i += 1
    a = rows - 1
    # 最后一行字符串
    while(a < len(s)):
        res[k] = s[a]
        k += 1
        a += interval
    return ''.join(res)
print zigzag('PAYPALISHIRING', 4)
