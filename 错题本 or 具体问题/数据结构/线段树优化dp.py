'''
例题: https://www.lanqiao.cn/problems/19853/learning/?contest_id=207

题意提取:  给出一个长为n 的数组 nums,   [a,b,c...]
a代表第一个物品的价格是a  ...
然后,在给出长为m的二维数组 ss, [(l1, r1, v1), (l2, r2, v2), ...]  其中的单个元素代表一种捆绑销售,  l1, r1, v1 分别代表第l1个物品到第r1个物品的总价格是v1
求, nums中的每个物品,至少购买一个, 最低花费多少钱?

2024年9月22日16:23:04,  同类题目 和 答案 https://codeforces.com/contest/115/submission/246106390
cf 2500分

'''

'''c++  答案
#include <iostream> 
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 100005;

long long dp[N];
struct node {
    long long val;
} tree[4*N];

void pushup(int rt) {
    tree[rt].val = min(tree[rt*2].val, tree[rt*2+1].val);
}
// 区间查询
long long query(int L, int R, int l, int r, int rt) {
    if (L <= l && R >= r)
        return tree[rt].val;
    int m = (l+r)/2;
    long long ans1 = 9e18, ans2 = 9e18;
    if (L <= m)
        ans1 = query(L, R, l, m, rt*2);
    if (R >= m+1)
        ans2 = query(L, R, m+1, r, rt*2+1);
    return min(ans1, ans2);
}
// 单点更新
void update(int L, long long C, int l, int r, int rt) {
    if (L == l && L == r) {
        tree[rt].val = C;
        return;
    }
    int m = (l+r)/2;
    if (L <= m)
        update(L, C, l, m, rt*2);
    if (L >= m+1)
        update(L, C, m+1, r, rt*2+1);
    pushup(rt);
}

struct pos {
  int a,b,c;
} p[N*2];

bool cmp(pos &p1, pos &p2) {
  return p1.b < p2.b;
}

int main() {
  int n,m,x;
  cin>>n>>m;
  for (int i=1; i<=n; i++)
    cin >> x, p[i].a = p[i].b = i, p[i].c = x; // 把单个的价值看也做长度为1的区间
  for (int i=1; i<=m; i++)
    cin >> p[n+i].a >> p[n+i].b >> p[n+i].c;
  sort(p+1, p+1+n+m, cmp);
  memset(dp, 0x7f, sizeof dp);
  dp[1] = 0; // 1位置空出来
  update(1, 0, 1, n+1, 1);
  for (int i=1; i<=n+m; i++)
    dp[p[i].b+1] = min(dp[p[i].b+1], query(p[i].a, p[i].b, 1, n+1, 1) + p[i].c),
      update(p[i].b+1, dp[p[i].b+1], 1, n+1, 1); // 逐个建树 每次都更新 略有些丑陋
  cout<<dp[n+1]<<'\n';
  
  return 0;
}
'''