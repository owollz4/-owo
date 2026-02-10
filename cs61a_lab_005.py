# Q2：插入元素
# 编写一个函数，它接受一个列表 s，以及两个值 before 和 after。它将 after 插入到 s 中每个值为 before 的元素之后。它返回 s。
# 重要提示: 不允许创建或返回新的列表。
# 请注意： 如果传入 before 和 after 的值相等，请确保在迭代时不会创建无限长的列表。
# 如果代码运行时间过长（超过几秒），可能是因为函数进入了插入新值的无限循环。
def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    lens = len(s)
    i = 0
    while i < lens:
        if s[i] == before and i == len(s) - 1:
            s.append(after)
            return s
        if s[i] == before:
            s.insert(i + 1, after)
            i += 1
            lens += 1
        i += 1

    return s
#Q2完成awa


# Q3: Group By
# 编写一个函数，它接受一个列表 s 和一个函数 fn 并返回一个字典。
# 字典的值是由 s 中元素组成的列表。
# 列表中的每个元素 e 都应满足 fn(e) 的返回值对于该列表中的所有元素均相同。
# 每个列表的键应为 fn(e) 的返回值。对于 s 中的每个元素 e，检查调用 fn(e) 返回的值，并将 e 添加到相应的组。

def group_by(s, fn):
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for i in range(len(s)):
        key = fn(s[i])
        if key in grouped:
            grouped[key].append(s[i])
        else:
            grouped[key] = [s[i]]
    return grouped
#Q3完成，虽然有点绕...


# Q5: 计数出现次数
# 实现 count_occurrences，它接受一个迭代器 t、一个整数 n 和一个值 x。它返回 t 的前 n 个元素中等于 x 的元素数量。
def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for _ in range(n):
        temp = next(t)
        if temp == x:
            count += 1
    return count
#Q5完成awa
#Emmm...虽然一开始想复杂了＞﹏＜，但还完成的不错，不是吗？awa

# Q6: Repeated
# 实现 repeated 函数，它接受一个迭代器 t 和一个大于 1 的整数 k。 它返回迭代器t中，第一个连续出现 k 次的值。
# 注意： 只调用最少次数的next(t)。 假设迭代器t中，至少存在一个元素连续重复k次。
# 小提示：如果您收到 StopIteration 异常，则您的 repeated 函数调用 next 的次数过多。
def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"

    count = 1
    current = next(t)
    while True:
        if count == k:
            return current
        nxt = next(t)
        if current == nxt:
            count += 1
        else:
            count = 1
        current = nxt
#Q6完成啦！awa

#以下是选做题，我打算看完一遍cs61a后，再做选做题owo






# def sprout_leaves(t, leaves):
#     """Sprout new leaves containing the labels in leaves at each leaf of
#     the original tree t and return the resulting tree.
#
#     >>> t1 = tree(1, [tree(2), tree(3)])
#     >>> print_tree(t1)
#     1
#       2
#       3
#     >>> new1 = sprout_leaves(t1, [4, 5])
#     >>> print_tree(new1)
#     1
#       2
#         4
#         5
#       3
#         4
#         5
#
#     >>> t2 = tree(1, [tree(2, [tree(3)])])
#     >>> print_tree(t2)
#     1
#       2
#         3
#     >>> new2 = sprout_leaves(t2, [6, 1, 2])
#     >>> print_tree(new2)
#     1
#       2
#         3
#           6
#           1
#           2
#     """
#     "*** YOUR CODE HERE ***"
#
#
# def partial_reverse(s, start):
#     """Reverse part of a list in-place, starting with start up to the end of
#     the list.
#
#     >>> a = [1, 2, 3, 4, 5, 6, 7]
#     >>> partial_reverse(a, 2)
#     >>> a
#     [1, 2, 7, 6, 5, 4, 3]
#     >>> partial_reverse(a, 5)
#     >>> a
#     [1, 2, 7, 6, 5, 3, 4]
#     """
#     "*** YOUR CODE HERE ***"
#
#
#
# # Tree Data Abstraction
#
# def tree(label, branches=[]):
#     """Construct a tree with the given label value and a list of branches."""
#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [label] + list(branches)
#
# def label(tree):
#     """Return the label value of a tree."""
#     return tree[0]
#
# def branches(tree):
#     """Return the list of branches of the given tree."""
#     return tree[1:]
#
# def is_tree(tree):
#     """Returns True if the given tree is a tree, and False otherwise."""
#     if type(tree) != list or len(tree) < 1:
#         return False
#     for branch in branches(tree):
#         if not is_tree(branch):
#             return False
#     return True
#
# def is_leaf(tree):
#     """Returns True if the given tree's list of branches is empty, and False
#     otherwise.
#     """
#     return not branches(tree)
#
# def print_tree(t, indent=0):
#     """Print a representation of this tree in which each node is
#     indented by two spaces times its depth from the root.
#
#     >>> print_tree(tree(1))
#     1
#     >>> print_tree(tree(1, [tree(2)]))
#     1
#       2
#     >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
#     >>> print_tree(numbers)
#     1
#       2
#       3
#         4
#         5
#       6
#         7
#     """
#     print('  ' * indent + str(label(t)))
#     for b in branches(t):
#         print_tree(b, indent + 1)
#
# def copy_tree(t):
#     """Returns a copy of t. Only for testing purposes.
#
#     >>> t = tree(5)
#     >>> copy = copy_tree(t)
#     >>> t = tree(6)
#     >>> print_tree(copy)
#     5
#     """
#     return tree(label(t), [copy_tree(b) for b in branches(t)])

