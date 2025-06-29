'''
原题:https://ac.nowcoder.com/acm/contest/73202/C

'''
#输入是一个列表,输出是 操作列表, 通过执行其中所有的交换操作,可以让输出列表变成排好序的. 后者说,让old变成new的操作
oo = old = [33,4,5,6,5,99,8,5]
old_i = [(x,str(i)) for i,x in enumerate(old, 0)] #也可以从1开始计数,,,错误,这里的开始没有意义,只是唯一标志,与编号无关;注意str转化
old = [b for a,b in old_i]
new = [b for a,b in sorted(old_i)]
print(old) #['0', '1', '2', '3', '4', '5', '6', '7']
print(new) #['1', '2', '4', '7', '3', '6', '0', '5']
#成功转化成了唯一str编号
d = {}
for i, x in enumerate(old):
    d[i] = x
    d[x] = i    #双向连接
n = len(old)
ans = []
for i in range(n):
    if old[i] != new[i]:
        find = d[new[i]]
        goal = i  #因为从前往后进行,所以goal一定更小
        if i != find:   #相等不用交换
            ans += (i + 0, find + 0),   #这里的0才是关系到编号起点
        #更新d的信息:  原本: d[i]对应old[i] d[find]对应new[find]
        #乱了,定位到了混乱点!!!
        #抓住重点!  需要更新的是d,也只有d   对应  d[find], d[goal] 是字母(str标志)  find和goal是编号
        d[find], d[goal] = d[goal], d[find]
        d[d[goal]], d[d[find]] = goal, find   #更新反向连接
print(ans) #[(0, 1), (1, 2), (2, 4), (3, 7), (4, 7), (5, 6), (6, 7)]
#验证交换操作
for g, t in ans:
    oo[g], oo[t] = oo[t], oo[g]
print(oo)   #验证完成,确实完成排序!

###真的有化简!  下面为原题的答案:  如果搞清楚映射的使用方向,就可以单向了.  当然,我还需要再调试...
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n in [1, 2]:
        print("YES")
        print(0)
        continue
    narr = [(num, i) for i, num in enumerate(arr)]
    narr.sort()
    s = narr[0][0] + narr[-1][0]
    for i in range(n + 1 >> 1):
        if narr[i][0] + narr[n - 1 - i][0] != s:
            print("NO")
            break
    else:
        target = [0] * n
        for i in range(n):
            target[narr[i][1]] = i
        ans = []
        for i in range(n):
            j = target[i]
            while j != i:
                ans.append((i + 1, j + 1))
                target[j], j = j, target[j]
        print("YES")
        print(len(ans))
        for i, j in ans:
            print(i, j)


# 2025-5-18 10:50:41 两两交换的最小次数：
# https://blog.csdn.net/Xuebing_han/article/details/103568689
'''
计算其中环的个数
对包含k个元素的环， 需要k-1次交换， 即k-1个边


'''
