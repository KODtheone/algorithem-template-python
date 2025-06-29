'''
2024年8月3日21:40:26
 atcoder的题目 :  https://atcoder.jp/contests/abc365/tasks/abc365_e   E - Xor Sigma Problem
被我给抄到题解了:   https://www.geeksforgeeks.org/sum-of-xor-of-all-subarrays/
geeksforgeeks 神奇的网站!!!

Sum of XOR of all subarrays
复杂度 O(n)
方法: 位运算, 假设有s个区间xor值, 起第i位个bit为1 ,则它贡献的和为 sum += (2^i * s)
对每一位i, 当第j个数字带有这一位时, i位是0或1就会发生反转.t代表从0到j位为开始, j为结尾的这一段,xor值为1的个数; 出现1时, t = j + 1 - t, 表示从0到j这个j+1个数字段都可贡献1, 而下次再遇到1, 依然反转,还是 t = j + 1 - t...
数字的bitlength不是很大, 比如30, 所以其实这个方法的复杂度是 O(30n)
# 贡献法 ,大概属于

扩展 or 也能同理计算 有1: t = j + 1
'''

# 参数: 数组 arr   返回值: 所有子数组的异或和的和(包括了 一个sum(arr) )
def findXorSum(arr):
    n = len(arr)
    ans = 0
    for i in range(30):
        t = 0
        for j in range(n):
            if arr[j] >> i & 1 == 1:
                t = j + 1 - t
            ans += t << i
    return ans
