''''
2024年11月15日10:19:38
bisect 说明:

i = bisect_right(a, x)  找到的i是第一个大于x的元素的索引
i = bisect_left(a, x)   找到的i是第一个大于等于x的元素的索引

'''
import bisect

a = [1, 2, 3]
print(bisect.bisect_right(a, 2))
print(bisect.bisect_left(a, 2))