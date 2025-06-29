'''
2024年11月24日14:40:40
题目 https://atcoder.jp/contests/abc381/tasks/abc381_g
来自一场abc 的 G题...    abc啊, 只有3个做出来...

题解: https://atcoder.jp/contests/abc381/editorial/11416
纯数学的结论  这玩意有人能当场推出来吗?

1≤N≤10^18


'''

'''
题解 md
官方

[G - 斐波那契乘积](/contests/abc381/tasks/abc381_g) 编辑：[en/_translator](/users/en_translator)
------------------------------------------------------------------------------------------------------------

* * *

#### 准备： $\sqrt{5}$ 的邻接。

如前所述， $a_n$ 的明式可以用一些常数 $c_1$ 和 $c_2$ 来表示：

$$
a_n = c_1 \left(\frac{1 + \sqrt{5}}{2}\right)^n + c_2 \left(\frac{1 - \sqrt{5}}{2}\right)^n.
$$

虽然我们想用这个漂亮的公式来解决问题，但在表示 $\sqrt{5} \bmod 998244353$ 时，问题出现了。如果在模数 $998244353$ 世界中存在 $\sqrt{5}$ ，即存在一个整数 $n$ ，使得 $n^2 = 5 \pmod{998244353}$ ，那么我们就可以用 $n$ 替换 $\sqrt{5}$ ，但遗憾的是，这样的 $n$ 并不存在。

僵局？不，我们可以用一个叫做**连接**的数学概念来解决这个问题。粗略地说，我们可以用下面的形式来处理这个值：（modint998244353）+（modint998244353） $\times \sqrt{5}$ ，这实际上就像处理普通的 modint998244353 一样。这样的代数结构被称为" $\sqrt{5}$ 邻接得到的场"。

- 更正式一点说，对于算术运算定义正确的 $F = \lbrace a + b \sqrt{5} \vert a, b \in F_{998244353} \rbrace$ 来说， $F$ 可以被证明构成一个域，因此任何针对域的算法也可以应用于 $F$ 。

在高级问题的求解中偶尔会出现接合（尤其以 $1$ 的 $k$ -th 根的接合最为典型），因此值得学习。

#### 解

从现在起，将一个值视为 $F = \lbrace a + b \sqrt{5} \vert a, b \in F_{998244353} \rbrace$ 的元素。

$a_n$ 可以表示为

$$
a_n = c_1 A^n + c_2 B^n
$$

对于一些常数 $A, B, c_1$ 和 $c_2$ 。(通过求出 $n=1, 2$ 的等式，可以求出 $c_1$ 和 $c_2$ ）。

设 $\mathrm{mod} = 998244353$ 。我们可以断言

$$
A^{2(\mathrm{mod} + 1)} = B^{2(\mathrm{mod} + 1)} = 1,
$$

所以序列 $a_n$ 的周期是 $2(\mathrm{mod} + 1)$ 的整除。因此，如果 $N \gt 2(\mathrm{mod} + 1)$ ，答案为 $N = 2 (\mathrm{mod} + 1)$ 的 $q$ 幂乘以答案为 $N = r$ 的 $N = q \times 2 (\mathrm{mod} + 1) + r$ 。因此，我们只需解决 $N \leq 2 (\mathrm{mod} + 1)$ 的问题即可。从现在起，我们假设 $N \leq 2 (\mathrm{mod} + 1)$ 。

设 $D = \frac{A}{B}$ ，则

$$
\frac{a_n}{B^n} = c_1 D^n + c_2,
$$

因此，只需计算 $\prod_{n=1}^N (c_1 D^n + c_2)$ 即可求出所求表达式的值；让我们考虑一下如何求值。

让 $M = \lfloor \sqrt{N} \rfloor$ .如果我们能求解 $N = M^2$ 的情况，那么只需找到 $\mathrm{O}(\sqrt{N})$ 更多的元素 $a_n$ 即可求得答案，因此下面我们考虑 $N = M^2$ 的情况。

$$
 \begin{aligned} &\prod_{n=1}^{M^2} (c_1 D^n + c_2) \\ &= \prod_{i=0}^{M-1} \prod_{j=1}^{M} (c_1 D^{iM + j} + c_2) \\ &= \prod_{i=0}^{M-1} \left\vert \prod_{j=1}^M (c_1 D^j X + c_2) \right \vert_{X=D^{iM}}. \end{aligned} 
$$

这里， $\vert f(X) \vert_{X=n}$ 意味着将 $X=n$ 赋值给 $f(X)$ 。设 $F(X) = \prod_{j=1}^M (c_1 D^j X + c_2)$ ，则需要通过以下两个步骤找到所求值：

1. 扩展 $F(X)$ ；
2. 在 $X = D^0, D^M, D^{2M}, \dots, D^{M(M-1)}$ 处对 $F(X)$ 进行求值。

我们将对每个步骤进行说明。

前一步可以通过二进制提升的方式在 $\mathrm{O}(M \log M)$ 中完成。

让 $F_n(X) = \prod_{j=1}^n (c_1 D^j X + c_2)$ 。我们要找到的是 $F_M(X)$ 。  
如果 $M$ 是偶数，我们就有下面的关系：

$$
 \begin{aligned} F_M(X) &= \prod_{j=1}^M (c_1 D^j X + c_2) \\ &= \prod_{j=1}^{M/2} (c_1 D^j X + c_2) \prod_{j=M/2+1}^M (c_1 D^j X + c_2) \\ &= F_{M/2}(X) F_{M/2} (D^{M/2} X). \end{aligned} 
$$

这样我们就可以在 $\mathrm{O}(M \log M)$ 时间内根据 $F_{M/2}(X)$ 找到 $F_M(X)$ 。如果 $M$ 是奇数，我们可以使用关系 $F_M(X) = F_{M-1}(X) (c_1 D^M X + c_2)$ 。这样， $F_M(X)$ 的展开总共需要 $\mathrm{O}(M \log M)$ 个时间。

现在我们考虑后一步。它主要要求对几何序列上的多项式进行多点求值。普通的多点求值需要花费 $\mathrm{O}(n \log^2 n)$ 时间，其中 $n$ 是多项式的阶数和要求值的点数，而在几何序列上进行多点求值只需 $\mathrm{O}(M \log M)$ 时间，算法名为**chirp z-transform**。[《Kyopro 算法百科全书》（日文）中的文章](https://noshi91.github.io/algorithm-encyclopedia/chirp-z-transform)，[《CodeForces》（英文）中的文章](https://codeforces.com/blog/entry/83532)。

通过适当的实施，原问题总共可以在 $\mathrm{O}(\sqrt{\mathrm{mod}} \log \mathrm{mod})$ 个时间内求解，速度已经足够快了。

发布于: 2 天前
最后更新时间: 2 天前

'''












'''
让gpt尝试一下:

解答下面的问题, 使用python
### Problem Statement

Define a sequence $a_1, a_2, a_3, \dots$ as follows:

$a_n = \begin{cases} x & (n=1) \\ y & (n=2) \\ a_{n-1} + a_{n-2} & (n \geq 3) \\ \end{cases}$

Find $\left( \displaystyle \prod_{i=1}^N a_i \right) \bmod{998244353}$.

You are given $T$ test cases to solve.

### Constraints

-   $1 \leq T \leq 5$
-   $1 \leq N \leq 10^{18}$
-   $0 \leq x \leq 998244352$
-   $0 \leq y \leq 998244352$
-   All input values are integers.

## 利用下面的结论编写程序:
Official

[G - Fibonacci Product](/contests/abc381/tasks/abc381_g) Editorial by [en\_translator](/users/en_translator)
------------------------------------------------------------------------------------------------------------

* * *

#### Preparation: adjunction of $\sqrt{5}$

As already known, the explicit formula of $a_n$ can be represented using some constants $c_1$ and $c_2$ as:

$$
a_n = c_1 \left(\frac{1 + \sqrt{5}}{2}\right)^n + c_2 \left(\frac{1 - \sqrt{5}}{2}\right)^n.
$$

Although we want to use this beautiful formula to solve the problem, the issue arises when it comes to representing $\sqrt{5} \bmod 998244353$. If there is $\sqrt{5}$ in the modulo-$998244353$ world, i.e. there exists an integer $n$ such that $n^2 = 5 \pmod{998244353}$, then we can replace $\sqrt{5}$ with $n$, but unfortunately, such an $n$ does not exist.

Stalemate? No. It can be resolved by a mathematical concept called **adjunction**. Roughly speaking, we can manage the value in the following form: (modint998244353) + (modint998244353) $\times \sqrt{5}$, which can actually be handled just as the ordinary modint998244353. Such an algebraic structure is called a “field obtained by adjoining $\sqrt{5}$.”

-   A bit more formally, for $F = \lbrace a + b \sqrt{5} \vert a, b \in F_{998244353} \rbrace$ with arithmetic operations properly defined, $F$ can be proven to form a field, so any algorithm against a field can be applied against $F$ too.

Adjunction occasionally occur in solutions of advanced problems (especially, adjunction of the $k$\-th root of $1$ is typical), so it is worth learning.

#### Solution

From now on, consider that a value is an element of $F = \lbrace a + b \sqrt{5} \vert a, b \in F_{998244353} \rbrace$.

$a_n$ can be represented as

$$
a_n = c_1 A^n + c_2 B^n
$$

for some constants $A, B, c_1$, and $c_2$. ($c_1$ and $c_2$ can be found by evaluating the equation for $n=1, 2$.)

Let $\mathrm{mod} = 998244353$. Nontrivally, we can assert that

$$
A^{2(\mathrm{mod} + 1)} = B^{2(\mathrm{mod} + 1)} = 1,
$$

so the period of the sequence $a_n$ is a divisor of $2(\mathrm{mod} + 1)$. Thus, if $N \gt 2(\mathrm{mod} + 1)$, the answer the $q$\-th power of the answer for $N = 2 (\mathrm{mod} + 1)$, multiplied by the answer for $N = r$, where $N = q \times 2 (\mathrm{mod} + 1) + r$. Thus, it is sufficient if we can solve the problem for $N \leq 2 (\mathrm{mod} + 1)$. From no on, we assume $N \leq 2 (\mathrm{mod} + 1)$.

Let $D = \frac{A}{B}$; then

$$
\frac{a_n}{B^n} = c_1 D^n + c_2,
$$

so it is sufficient to compute $\prod_{n=1}^N (c_1 D^n + c_2)$ to evaluate the sought expression; let us consider how to evaluate it.

Let $M = \lfloor \sqrt{N} \rfloor$. If we can solve the case for $N = M^2$, all that left is to find $\mathrm{O}(\sqrt{N})$ more elements $a_n$ to find the answer, so hereinafter we consider $N = M^2$ case.

$$
 \begin{aligned} &\prod_{n=1}^{M^2} (c_1 D^n + c_2) \\ &= \prod_{i=0}^{M-1} \prod_{j=1}^{M} (c_1 D^{iM + j} + c_2) \\ &= \prod_{i=0}^{M-1} \left\vert \prod_{j=1}^M (c_1 D^j X + c_2) \right \vert_{X=D^{iM}}. \end{aligned} 
$$

Here, $\vert f(X) \vert_{X=n}$ means assigning $X=n$ to $f(X)$. Let $F(X) = \prod_{j=1}^M (c_1 D^j X + c_2)$, then the following two steps are required to find the sought value:

1.  expand $F(X)$;
2.  evaluate $F(X)$ at $X = D^0, D^M, D^{2M}, \dots, D^{M(M-1)}$.

We explain each step.

The former step can be accomplished in a total of $\mathrm{O}(M \log M)$ in the manner of binary lifting.

Let $F_n(X) = \prod_{j=1}^n (c_1 D^j X + c_2)$. What we want to find is $F_M(X)$.  
If $M$ is even, we have the following relation:

$$
 \begin{aligned} F_M(X) &= \prod_{j=1}^M (c_1 D^j X + c_2) \\ &= \prod_{j=1}^{M/2} (c_1 D^j X + c_2) \prod_{j=M/2+1}^M (c_1 D^j X + c_2) \\ &= F_{M/2}(X) F_{M/2} (D^{M/2} X). \end{aligned} 
$$

This allows us to find $F_M(X)$ based on $F_{M/2}(X)$ in $\mathrm{O}(M \log M)$ time. If $M$ is odd, we can use the relation $F_M(X) = F_{M-1}(X) (c_1 D^M X + c_2)$. By implementing them, $F_M(X)$ can be expanded in a total of $\mathrm{O}(M \log M)$ time.

Now we consider the latter step. It essentially asks to do multi-point evaluation of a polynomial on a geometric sequence. While an ordinary multi-point evaluation costs $\mathrm{O}(n \log^2 n)$ time, where $n$ is the degree of the polynomial and the number of points to evaluate, but that on a geometric sequence can be done in $\mathrm{O}(M \log M)$ time with an algorithm called **chirp z-transform**. [Article in Kyopro Encyclopedia of Algorithms (Japanese)](https://noshi91.github.io/algorithm-encyclopedia/chirp-z-transform), [Article in CodeForces (English)](https://codeforces.com/blog/entry/83532).

By implementing it appropriately, the original problem can be solved in a total of $\mathrm{O}(\sqrt{\mathrm{mod}} \log \mathrm{mod})$ time, which is fast enough.
'''