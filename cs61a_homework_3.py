# Q1：Num Eights
# 编写一个递归函数 num_eights，该函数接受一个正整数 n 并返回数字 8 在 n 中出现的次数。
# 注意： 使用递归；如果使用了赋值语句或者循环，测试将无法通过。（但是，可以使用函数定义来实现。）
def num_eights(n):
    
    if n < 10:
        return 1 if n == 8 else 0
    return (1 if n % 10 == 8 else 0) + num_eights(n // 10)

# print(num_eights(888))

# Q2：Digit Distance
# 对于给定的整数，digit distance 指的是一个数中，相邻两位数字之差的绝对值的总和。例如：
# 6 的 digit distance 为 0。
# 61 的 digit distance 为 5，因为 6 - 1 的绝对值为 5。
# 71253 的 digit distance 为 12 (6 + 1 + 3 + 2)。
# 写一个函数来计算给定正整数的 digit distance。你必须使用递归，否则测试将失败。.
def digit_distance(n):
    if(n < 10):
        return 0
    return digit_distance(n//10) + abs(n % 10-(n//10) % 10)
print(digit_distance(71253))

# Q3: 交错求和
# 编写一个名为 interleaved_sum 的函数，该函数接受一个数字 n 以及两个单参数函数 odd_func 和 even_func。此函数将 odd_func 应用于 1 到 n（包括 n）之间的每个奇数，将 even_func 应用于每个偶数，并返回总和。
# 例如，执行 interleaved_sum(5, lambda x: x, lambda x: x * x) 返回 1 + 2*2 + 3 + 4*4 + 5 = 29。
# 实现此函数，无需使用任何循环或直接判断数字的奇偶性——不允许使用模数 (%)！ 应该从 1 开始，因为它是一个奇数。
def interleaved_sum(n, odd_func, even_func):
    def go_next(k , current, next):
        if(k > n):
            return 0
        return go_next(k + 1, next, current) + current(k)
    return go_next(1 , odd_func, even_func)

print(interleaved_sum(5, lambda x: x, lambda x: x * x))


# Q4: 数硬币
# 给定一个正整数 total，如果硬币值的总和为 total，则一组硬币可以兑换 total。 在这里，我们将使用标准美国硬币值：1、5、10、25美分。
#例如，以下集合可以兑换 15：
# 15个1美分的硬币
# 10个1美分的硬币，1个5美分的硬币
# 5个1美分的硬币，2个5美分的硬币
# 5个1美分的硬币，1个10美分的硬币
# 3个5美分的硬币
# 1个5美分的硬币，1个10美分的硬币
#因此，15 有 6 种兑换方式。编写一个递归函数 count_coins，它接受一个正整数 total 作为输入，并返回用硬币凑出总金额 total 的组合数。
##############################
# 寄了，不会用递归的方式写，写个迭代的   -----(论屎山代码是怎么来的)   (滑稽)
def total_coin(coin):
    count = 0
    x,y,z,w = 0,0,0,0
    while(25*w <= coin):
        z = 0
        while(10*z <= coin):
            y = 0
            while(5*y <= coin):
                x = 0
                while(x <= coin):
                    if((x + 5*y + 10*z + 25*w) == coin):
                        count += 1
                    x += 1
                y += 1
            z += 1
        w += 1
    return count
print(total_coin(15))
        

