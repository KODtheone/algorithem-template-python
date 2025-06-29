'''
题解: https://leetcode.cn/problems/minimize-manhattan-distances/solutions/2716755/tu-jie-man-ha-dun-ju-chi-heng-deng-shi-b-op84/
曼哈顿距离排序:
例题: https://leetcode.cn/problems/minimize-manhattan-distances/
曼哈顿距离处理技巧: https://www.bilibili.com/video/BV1fq421A7CY/   旋转,去掉绝对值
#上面其实推导了一个经典结论：曼哈顿距离在坐标轴旋转 45 度后与切比雪夫距离等价。
2, 切比雪夫距离,只要比较x的差值 和 y的差值中 更大的一个就是了
'''
#坐标旋转 再×根号2:  从原来的x,y 到 x+y, y-x;  如果是任意角,就需要sin 来算了...
x,y = x+y, y-x
# 转换后的两点距离:  max(dx, dy)

# 原题:
from sortedcontainers import *

class Solution:
    def minimumDistance(self, ps: List[List[int]]) -> int:
        sx = SortedList()
        sy = SortedList()
        for x, y in ps:
            sx.add(x+y)
            sy.add(y-x)
        ans = inf
        for x, y in ps:
            sx.remove(x+y)
            sy.remove(y-x)
            ans = min(ans, max(sx[-1]-sx[0], sy[~0]- sy[0]))
            sx.add(x+y)
            sy.add(y-x)
        return ans