def falling(n,k):
    product = 1
    while(k > 0):
        product = n*product
        k = k - 1
        n = n - 1
    return product

def divisible_by_k(n,k):
    m = n
    num = 0
    while(m):
        if(m % k == 0 ):
            print(m)
            num = num + 1
        m = m - 1

    if(m == 0):
        return num
        # print("一共有")
        # print(num)
        # print("小于或等于 n 且能被 k 整除的正整数")
    elif(m < 0):
        return ValueError 

def sum_digits(y):

    total = 0
    while y > 0:
        total = total + (y % 10)
        y = y // 10
        # 要理解这段代码，首先需要理解两个关键的算术运算符是如何在十进制数上发挥作用的：
        # 取模运算 (% 10)：获取数字的最后一位。
        # 任何一个整数除以 10，余数必然是个位上的数字。
        # 例如：123 % 10 的结果是 3（因为 123 = 12×10 + 3）。
        # 整除运算 (// 10)：去掉数字的最后一位。
        # 整除会舍去小数部分，相当于将数字向右移动一位（砍掉个位）。
        # 例如：123 // 10 的结果是 12。
    return total

    
print(sum_digits(123))
# a = divisible_by_k(7,3)
# # print("一共有")
# print("一共有",a,"个小于或等于 n 且能被 k 整除的正整数")
# # print("个小于或等于 n 且能被 k 整除的正整数")