'''
例题: https://leetcode.cn/problems/sum-of-number-and-its-reverse/description/
反转数例如  123, 321   和 为 444 则 444返回True
logn 做法:
双指针  递归 或者 递推.  这么说起来, 有点像是  dp,   数位dp...

另, 计算k进制下 拆分方式的情况数:  例题: https://www.luogu.com.cn/problem/P3276

'''

# 递推
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        nums = list(map(int, list(str(num))))

        def check(i, j, p, b):
            while i < j:
                head = p * 10 + nums[i]
                if head <= 18 and (head + b) % 10 == nums[j]:
                    p, b = 0, (head + b) // 10
                elif head > int(i == 0) and (head - 1 + b) % 10 == nums[j]:
                    p, b = 1, (head - 1 + b) // 10
                else:
                    return False
                i += 1
                j -= 1
            return (nums[i] - b) % 2 == 0 if i == j else p == b

        return check(0, len(nums) - 1, 0, 0) or (nums[0] == 1 and check(1, len(nums) - 1, 1, 0))


# 递归
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        nums = list(map(int, list(str(num))))

        def dfs(i, j, p, b):
            if i == j:
                return (nums[i] - b) % 2 == 0
            if i == j + 1:
                return p == b
            head = p * 10 + nums[i]
            if head <= 18 and (head + b) % 10 == nums[j]:
                return dfs(i + 1, j - 1, 0, (head + b) // 10)
            elif head > int(i == 0) and (head - 1 + b) % 10 == nums[j]:
                return dfs(i + 1, j - 1, 1, (head - 1 + b) // 10)
            return False

        return dfs(0, len(nums) - 1, 0, 0) or (nums[0] == 1 and dfs(1, len(nums) - 1, 1, 0))

'''
定义 f(i,j,pre,suf) 为在满足下列条件的情况下，数字 N 中的子数字序列 N[i..j] （下标从 0 开始）是否可以由两个互为逆序的数字 K，reverse(K) 相加而来，其中：
如果 pre=1，表示相加的结果需要向左侧进一位，进位完成之后剩下的结果和 N[i...j] 相同；
如果 suf=1，表示在两数相加之前，已经有从低位传来的进位，相加结果需要把这个进位考虑进去。
举例说明：对于数字 12345，f(1,3,1,1) 表示，是否能找到三位数 k ，使得 k+erverse(k)+ 进位的 1 = 1234（去掉向高位进位的 1，剩下的结果和 num[1...3]=234 相同）。（注意下标从 0 开始）

'''