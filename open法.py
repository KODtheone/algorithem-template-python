'''
2024年6月21日16:58:09,  就像是 cf模板的板子, 偷鸡使用, 也有可能出问题...

'''

# a = list(map(int, input()[1:-1].split(",")))    # 读取数列
# b = input()                                     # 读取字符串
# x = int(input())                                # 读取整数
# a = [x.lstrip()[1:-1] for x in t[1:-1].split(",")]   # 读取字符列
# t = '["1", "a", "b"]'
# print(t)
# a = [x.lstrip()[1:-1] for x in t[1:-1].split(",")]
# print(a)

# f.write('['+ ','.join(map(str,ans)) + "]"+'\n') # 输出数列

f = open("user.out", "w")
while True:
    try:
        a = list(map(int, input()[1:-1].split(",")))
        ans = a[len(a) // 2:]
        f.write('['+ ','.join(map(str,ans)) + "]"+'\n')
    except:
        break
exit()