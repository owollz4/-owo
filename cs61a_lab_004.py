# Q2：除法
# 实现 divide 函数，该函数接收两个正整数列表 quotients 和 divisors 作为输入。 
# 函数返回一个字典，字典的键为 quotients 列表中的元素。 对于每一个键 q，其对应的值为一个列表，该列表包含 divisors 列表中所有能被 q 整除的元素。

def divide(quotients, divisors):
    """返回一个字典，字典中每个键 q 对应的值是一个列表，该列表包含了所有能被 q 整除的除数。

    >>> divide([3, 4, 5], [8, 9, 10, 11, 12])
    {3: [9, 12], 4: [8, 12], 5: [10]}
    >>> divide(range(1, 5), range(20, 25))
    {1: [20, 21, 22, 23, 24], 2: [20, 22, 24], 3: [21, 24], 4: [20, 24]}
    """
    
    return {key:[x for x in divisors if x % key == 0] for key in quotients }
# print(divide([3, 4, 5], [8, 9, 10, 11, 12]))

# Q3：购买水果
# 实现 buy 函数，它接受一个 required_fruits 列表（字符串）、一个 prices 字典（字符串作为键，正整数作为值）和一个 total_amount （整数）。
# 它会打印出所有购买方案，每种 required_fruits 中的水果至少购买一个，且总价等于 total_amount。
# 你必须包含 required_fruits 中的每种水果至少一个，并且不能包含任何不在 required_fruits 中的其他水果。
# display 函数会很有用。你可以对一个 fruit 及其 count 调用 display 来创建一个包含两者的字符串。
# fruits 和 amount 代表什么？它们在递归中是如何使用的？

def buy(required_fruits, prices, total_amount):
    """打印所有总价为 amount 的购买方案，每种水果至少购买一个。

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """
    return 1#我不会😅

# Q4: 距离
# 我们现在将实现函数 distance，该函数计算两个城市对象之间的距离。
# 回想一下，两个坐标对 (x1, y1) 和 (x2, y2) 之间的距离可以通过计算 (x1 - x2)**2 + (y1 - y2)**2 的 sqrt 来找到。
# 为了方便大家，我们已经导入了 sqrt 函数。
# 使用城市的纬度和经度作为坐标，你需要使用选择器来获取这些信息！
######make_city是一个自带的函数，但只有官方学生有，所以高仿了一下
def make_city(name,lat,lon):
    data = {1:name,2:lat,3:lon}
    return data
def get_name(city):
    return city[1]
def get_lat(city):
    return city[2]
def get_lon(city):
    return city[3]
from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    x1 = get_lat(city_a)
    x2 = get_lat(city_b)
    y1 = get_lon(city_a)
    y2 = get_lon(city_b)

    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
# city_a = make_city('city_a', 0, 1)
# city_b = make_city('city_b', 0, 2)
# print(distance(city_a, city_b))

# Q5：哪个城市更近
# 接下来，实现 closer_city 函数，该函数接受一个纬度、一个经度和两个城市，并返回离给定经纬度最近的城市的名字。
# 你只能使用前面介绍的选择器、构造器和你定义的 distance 函数。

def closer_city(lat, lon, city_a, city_b):
    """
    返回 city_a 或 city_b 的名称，以最接近坐标 (lat, lon) 的城市为准。如果两个城市与坐标的距离相同，则认为 city_b 是更近的城市。

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    x1 = get_lat(city_a)
    x2 = get_lat(city_b)
    y1 = get_lon(city_a)
    y2 = get_lon(city_b)
    distance1 = sqrt((x1 - lat)**2 + (y1 - lon)**2)
    distance2 = sqrt((x2 - lat)**2 + (y2 - lon)**2)
    if(distance1 < distance2):
        return city_a[1]
    elif(distance1 > distance2):
        return city_b[1]
    else: 
        return "all"
    return 0
# berkeley = make_city('Berkeley', 37.87, 112.26)
# stanford = make_city('Stanford', 34.05, 118.25)
# print(closer_city(38.33, 121.44, berkeley, stanford))