
#Q4：复合恒等函数
#编写一个函数，该函数接受两个单参数函数 f 和 g，并返回另一个函数，该函数具有一个参数 x。该函数在 f(g(x)) 等于 g(f(x)) 时返回 True。您可以假设 g(x) 的结果是 f 的有效输入，反之亦然。
def composite_identity(f, g):
    def compare(x):
        if (f(g(x)) == g(f(x))):
            return True
        else:
            return False
    return compare

# add_one = lambda x: x + 1        # 将 x 加一
# square = lambda x: x**2          # 对 x 求平方 [返回 x^2]
# b1 = composite_identity(square, add_one)
# print(b1(4))
#############################################################
# Q5：Count Cond
# 考虑以下 count_fives 和 count_primes 的实现，它们使用了之前作业中的 sum_digits 和 is_prime 函数：
def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
import math

def is_prime(n):
    """
    判断一个数是否为素数。
    """
    # 1. 处理小于等于1的数（非素数）
    if n <= 1:
        return False
    
    # 2. 处理2（最小的素数）
    if n == 2:
        return True
    
    # 3. 排除所有大于2的偶数
    if n % 2 == 0:
        return False
    
    # 4. 只需要检查从 3 到 sqrt(n) 的奇数
    # int(math.sqrt(n)) + 1 确保包含边界情况
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True

def count_cond(f):
    def count(n):
        i = 1
        num_of_count = 0
        while i <= n:
            if f(n,i):
                num_of_count += 1
            i += 1
        return num_of_count
    return count
is_i_prime = lambda n, i: is_prime(i)
count_primes = count_cond(is_i_prime)
count_fives = count_cond(lambda n, a: sum_digits(n * a) == 5)
print(count_fives(10))
print(count_primes(20))
