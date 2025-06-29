'''
2024年7月13日09:40:00
灵的分组循环模板   熟悉模式,能稍微提高效率吧,大概
例题: https://leetcode.cn/problems/find-if-array-can-be-sorted/solutions/2613051/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-j3nik/?envType=daily-question&envId=2024-07-13

2024年7月13日16:34:28, 分组循环,有些地方还是不如dp: 例题:https://codeforces.com/contest/1992/problem/D
用分组循环来做,需要区分 在水里 和 可以跳的两种状态  ;  而dp在遇到L 时,直接大范围更新, w就往前一个更新,  一次遍历就解决了

'''
n = len(nums)
i = 0
while i < n:
    start = i
    while i < n and ...:
        i += 1
    # 从 start 到 i-1 是一组
    # 下一组从 i 开始，无需 i += 1