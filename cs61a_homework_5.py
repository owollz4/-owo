# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


# Q1: 无穷冰雹序列
# 编写一个生成器函数，该函数产生以数字 n 开头的冰雹序列的元素。到达冰雹序列的末尾后，生成器应无限期地产生值 1。
# 以下是冰雹序列的定义：
# 选择一个正整数 n 作为开始。
# 如果 n 是偶数，则将其除以 2。
# 如果 n 是奇数，则将其乘以 3 并加 1。
# 继续此过程，直到 n 为 1。
# 尝试以递归方式编写此生成器函数。如果遇到困难，可以先尝试用迭代法编写，再考虑如何将其转化为递归实现。
# 提示： 因为 hailstone 返回一个生成器，所以你可以使用 yield from 语句来简化代码，直接从 hailstone 生成器中产生值！
def hailstone(n):
    """Q1: Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    while True:
        if n == 1:
            yield n
        if n % 2 == 0:
            n = n // 2
            yield n
        elif n % 2 == 1 and n > 1:
            n = n * 3 +1
            yield n
#迭代版写完了，递归版怎么写呢？
def hailstone(n):
    """Q1: Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n == 1:
        while True:
            yield n
    elif n % 2 == 0:
        yield from hailstone(n // 2)
    elif n % 2 == 1 and n > 1:
        yield from hailstone(n * 3 +1)
#递归版也写完了awa
#
# Q2: 合并生成器
# 编写一个生成器函数 merge，它接受两个无限生成器 a 和 b，它们按递增顺序排列且没有重复项，并返回一个生成器，该生成器具有两个生成器的所有元素，按递增顺序排列，且没有重复项。
def merge(a, b):
    """Q2:
        >>> def sequence(start, step):
        ...     while True:
        ...         yield start
        ...         start += step
        >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
        >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
        >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
        >>> [next(result) for _ in range(10)]
        [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    val_a = next(a)
    val_b = next(b)
    while True:
        if val_a < val_b:
            yield val_a
            val_a = next(a)
        elif val_b < val_a:
            yield val_b
            val_b = next(b)
        else:  # val_a == val_b，去重
            yield val_a
            val_a = next(a)
            val_b = next(b)


# Q3: yield_paths：生成树的路径
# 定义一个生成器函数 yield_paths(t, value)，该函数接收一棵树 t 和一个值 value，并生成从树根到所有标签为 value 的节点的路径。
#
# 每条路径应该是一个列表，包含从树根到目标节点路径上的所有标签。生成路径的顺序没有要求。

def yield_paths(t, value):
    """Q4: Yields all possible paths from the root of t to a node with the label
    value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = yield_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == value:
        yield
    for b in branches(t):
        for ____ in ____:
            yield ____
#寄了，不会qwq