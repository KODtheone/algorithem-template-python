'''
2024年8月19日10:32:24,这个技巧, 似乎不应该属于矩阵...   dp?
矩阵快速幂,  例题 https://leetcode.cn/problems/student-attendance-record-ii/solutions/2885136/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-a8kj/?envType=daily-question&envId=2024-08-19
552. 学生出勤记录 II
需要先想好转移矩阵, 后两维合并成一维, 也就是三维的变成两维的

矩阵快速幂部分可以当做一个板子
2024年8月19日12:31:09, 很神奇  ai写出来的板子就是正确的...
'''

def matrix_multiply(A, B, mod=None):
    """
    矩阵乘法
    :param A: 矩阵A
    :param B: 矩阵B
    :param mod: 模数，如果不需要取模则为None
    :return: A * B的结果
    """
    n = len(A)
    m = len(B[0])
    p = len(B)
    # 确保A的列数等于B的行数
    if len(A[0]) != p:
        raise ValueError("矩阵A的列数必须与矩阵B的行数相同")
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod if mod is not None else (result[i][j] + A[i][k] * B[k][j])
    return result

def matrix_power(A, n, mod=None):
    """
    矩阵快速幂
    :param A: 矩阵A
    :param n: 幂次
    :param mod: 模数，如果不需要取模则为None
    :return: A的n次幂的结果
    """
    # 单位矩阵
    result = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    while n > 0:
        # 如果n是奇数，则将当前A乘到结果上
        if n % 2 == 1:
            result = matrix_multiply(result, A, mod)
        # n除以2，A自乘
        A = matrix_multiply(A, A, mod)
        n = n // 2
    return result

# 示例
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    n = 5
    mod = 1000  # 可选的模数
    print("Matrix A^%d:" % n)
    print(matrix_power(A, n, mod))


# 纯享版
# 说明 mul 计算两个矩阵相乘, 是应用于 pow的;
def mul(a, b, mod) :
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*b)] for row in a]

def pow(a, n, mod):
    size = len(a)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1
    while n:
        if n & 1:
            res = mul(res, a, mod)
        a = mul(a, a, mod)
        n >>= 1
    return res

# 使用: 计算矩阵a的 n次方  pow(a, n, mod)


'''
2024年12月10日10:31:24,  矩阵快速幂 , 核心的思路跟 快速幂是一样的,  原理都是倍增    只不过加上了矩阵乘法的规则

例题2: https://leetcode.cn/problems/knight-dialer/
动态规划可以做到 O(n)
而使用矩阵快速幂 可以做到 O(logn)

'''
MOD = 1_000_000_007
# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)] for row in a]

# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        f0 = [[1], [1], [1], [1]]
        m = [[0, 1, 1, 0], [2, 0, 0, 0], [2, 0, 0, 1], [0, 0, 2, 0]]
        m = pow_mul(m, n - 1, f0)
        return (m[0][0] * 4 + m[1][0] * 2 + m[2][0] * 2 + m[3][0]) % MOD


'''
2025年5月5日10:56:00 ， 类似 斐波那契数列的递推  当n非常大的时候， 也可以使用 矩阵快速幂
例题： https://leetcode.cn/problems/domino-and-tromino-tiling/solutions/1968516/

'''
