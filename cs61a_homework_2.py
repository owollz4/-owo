#Q1：乘积
#请编写一个名为 product 的函数，该函数返回一个序列的前 n 项的乘积。具体来说，product 函数接受一个整数 n 和一个函数 term 作为参数，其中 term 是一个单参数函数，用于确定序列。（也就是说，term(i) 给出序列的第 i 项。）product(n, term) 应该返回 term(1) * ... * term(n)。
def product(n, term):
    number = 1
    while(n > 0):
        number = term(n) * number
        n = n - 1
    return number

def square(x):
    return x * x

# print(product(3,square))
##################
#Q2：累积
#接下来，我们来看看 product 函数是如何作为更通用的 accumulate 函数的一个特例：
def add(x,y):
    return x + y
def mul(x,y):
    return x * y
def accumulate(fuse, start, n, term):
    while(n > 0):
        start = fuse(start, term(n))
        n = n - 1
    return start
def div(x, y):
    return x / y
#print(accumulate(div, 11, 3, square))
##################
#Q3: Make Repeater
#实现函数 make_repeater，它接受一个单参数函数 f 和一个正整数 n 作为输入。 该函数返回一个新的单参数函数，对于输入 x，make_repeater(f, n)(x) 将返回将 f 应用于 x 迭代 n 次的结果，即 f(f(...f(x)...))。 例如，make_repeater(square, 3)(5) 的结果是将 5 平方三次，得到 390625，等同于 square(square(square(5)))。
def make_repeater(f, n):
    def repeater(x):
        result = x
        for _ in range(n):
            result = f(result)
        return result
    return repeater
a = make_repeater(square, 2)(5)
print(a)
    

