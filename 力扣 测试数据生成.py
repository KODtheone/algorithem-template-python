from random import *

#随机字符串
def gen_str(n):
    return ''.join([chr(randint(65, 90)) for i in range(n)])
def gen_abc(n):
    return ''.join([choice(["a","b","c"]) for i in range(n)])
#随机01串
def gen_01(n):
    return ''.join([choice(['0', '1']) for i in range(n)])
# 随机数字列表
def gen_nums(n = 100, mn = 1, mx = 10**3):
    return [randint(mn, mx) for i in range(n)]
# 随机二维数字列表
def gen_2d_nums(m = 100, n = 100, mn = 1, mx = 10**3):
    return [[randint(mn, mx) for j in range(n)] for i in range(m)]

# 随机数字字符串
def gen_nums_str(n = 10 ** 5, mn = 0, mx = 9):
    return "".join([str(randint(mn, mx)) for i in range(n)])

##
test = gen_nums_str()
print(test)

