# Q2: Print If
# 实现 print_if，它接受一个列表 s 和一个单参数函数 f。它会打印列表 s 中所有使得 f(x) 返回 True 的元素 x。
def print_if(s, f):
    """Print each element of s for which f returns a true value.

    >>> print_if([3, 4, 5, 6], lambda x: x > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda x: x % 2 == 0)
    4
    6
    >>> print(result)  # print_if should return None
    None
    """
    for x in s:
        if(f(x)):
            print(x)
    return 0
# print_if([3, 4, 5, 6], lambda x: x > 4)

# Q3: Close
# 实现 close，它接受一个数字列表 s 和一个非负整数 k。它会返回列表 s 中有多少个元素与它们的索引的差值小于等于 k。
def close(s, k):
    """Return how many elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        if(abs(s[i] - i) <= k):
            count += 1
    return count
# t = [6, 2, 4, 3, 5]
# print(close(list(range(10)), 0))

# Q5：接近列表
# 实现函数 close_list，它接受一个数字列表 s 和一个非负整数 k。 它返回列表 s 中所有与它们的索引的差的绝对值小于等于 k 的元素。 也就是说，对于列表中的每个元素，它与该元素索引的差的绝对值小于等于 k。
def close_list(s, k):
    """返回 s 中与其索引相差在 k 以内的元素的列表。

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # 只有 3 等于它的索引
    [3]
    >>> close_list(t, 1)  # 元素 2、3 和 5 与它们的索引的差的绝对值小于等于 1
    [2, 3, 5]
    >>> close_list(t, 2)  # 元素 2、3、4 和 5 与它们的索引的差的绝对值小于等于 2
    [2, 4, 3, 5]
    """
    return [s[x] for x in range(len(s)) if (abs(s[x] - x) <= k)]
# t = [6, 2, 4, 3, 5]
# print(close_list(t, 0))

# ！！！Q6：仅平方数
# 实现函数 squares，它接受一个正整数列表。 它返回一个新列表，该列表包含原列表中所有完全平方数的平方根。 使用列表推导式。

from math import sqrt

def squares(s):
    """返回一个新列表，其中包含原始列表中完全平方数的元素的平方根。

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(sqrt(s[n])) for n in range(len(s)) if (sqrt(s[n]) % 1 == 0 )]
seq = [8, 49, 8, 9, 2, 1, 100, 102]
print(squares(seq))

# Q7：双重 8
# 编写一个递归函数，输入一个正整数 n，判断其各位数字中是否包含两个相邻的 8。 不要使用 for 或 while。

def double_eights(n):
    """ 返回 n 是否有连续两个数字为 8。 假设 n 至少有两位数字。

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # 禁止迭代
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    if(n < 88):
        return False
    return True if n % 10 == 8 & (n // 10) % 10 == 8 else double_eights(n // 10)
# print(double_eights(538835))
# print(double_eights(89))

# Q8：制作洋葱
# 编写一个函数 make_onion，它接受两个单参数函数 f 和 g。 它返回一个函数，该函数接收三个参数 x、y 和 limit。如果通过最多 limit 次调用函数 f 和 g，能够从 x 得到 y，则返回的函数返回 True；否则返回 False。
# 例如，如果函数 f 的作用是加 1，函数 g 的作用是乘以 2，那么可以通过四次调用从 5 得到 25：f(g(g(f(5))))。
def make_onion(f, g):
    """返回一个名为 can_reach(x, y, limit) 的函数。该函数判断是否可以通过仅使用函数 f、g 和初始值 x，且最多调用 limit 次函数，来得到结果 y。

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # 做不到
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # 做不到
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach
# up = lambda x: x + 1
# double = lambda y: y * 2
# can_reach = make_onion(up, double)
# print(can_reach(5, 25, 4))