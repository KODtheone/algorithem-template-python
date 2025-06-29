'''
例题:https://www.lanqiao.cn/problems/19931/learning/?contest_id=212
4. 小鸡变鸡腿

2024年11月2日16:40:03,  题意:  构造后二分

题意,  确实是二分, 但是, 并不是n越大, 可能数就越大 ,而是根据质因数分解数来决定的
构造方法: 从1开始构造, 直到出现大于题目给出的 10**18种的数字.
另外, 每当新数的情况数大于上一个极大值, 都记录下来, 然后再继续构造

'''



# 解法:
times = 1  # 0有t, 1无t
if not times:
    times = ix()
for _ in range(times):
    tmp = [0]
    val = [0]
    for i in range(1, 10001):
        v = i
        c = 1
        for j in range(2, i + 1):
            if j * j > i: break
            x = 0
            while v % j == 0:
                x += 1
                v //= j
            c *= x * i + 1
        if v > 1:
            c *= i + 1
        if c > val[-1]:
            tmp.append(i)
            val.append(c)
print(tmp)
print(val)
t = ix()
for i in range(t):
    k = ix()
    print(tmp[bisect_left(val, k)])