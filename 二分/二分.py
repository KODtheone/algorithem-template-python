"""
虽然都可以用 bisect 但是写二分比较直观  当然,核心是判断函数,所以我这里两种模板都写一下吧
例题: https://leetcode.cn/problems/split-array-largest-sum/

"""
from bisect import bisect_right


def check(m):  # m值为 mid, 需要验证能否成立
    # 根据题目要求（难点）
    return True  # 或者 return False

# def bin_int_search(l, r):
def bs(l, r):
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return r  ## r = l 为bisect_right  或者  return mid  为bisect_left ##2024年5月5日15:43:38,似乎有问题,下面的ffftttt考虑是正确的
    #如果答案出来有时差1, 有时正确,那就是这里需要更换
    ##对 fffffttttttttt的形式直接使用,返回值是第一个t的位置;
    # 对于tttttttttfffffffff 则用 not check() 转换成ffffffttttttttttt, 而想要返回原版的最后一个t, 则return r - 1


#纯享版
def check(m):
    #
    return True  #

def bs(l, r):
    while l < r:
        mid = (l + r) >> 1
        if check(mid):      r = mid
        else:               l = mid + 1
    return r

'''节省纯
#  fffttttt 直接用
def check(m):
    
    return True  

l, r = 
while l < r:
    mid = (l + r) >> 1
    if check(mid):      r = mid
    else:               l = mid + 1
return r

# 对ttttffff 需要取反
def check(m):
    
    return True  

l, r = 
while l < r:
    mid = (l + r) >> 1
    if not check(mid):      r = mid
    else:               l = mid + 1
return r - 1

'''




##使用bisect的方式, 需要让答案前的全是False  答案后是True
##但是不对劲, 用bisect 会造成 mle
def check(mid):
    return True

ans = list(range(l,r+1))[bisect_right(list(range(l,r+1)), False, key = check) ]
# bisect_right(range(l,r+1), True, key = check)  #也可以 key = lambda x:x... 用匿名函数

# 2024年12月3日20:07:13 , 我好像知道问题了:  如果 l, r的范围很大, 那么 光是构造list(range(l,r+1)) 就mle了  , 所以需要离散



