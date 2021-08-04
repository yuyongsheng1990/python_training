# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> Fib
# @Time: 2021/8/4 17:52 
# @Author: Yu Yongsheng
# @Description: 斐波那契数列

# 递归实现
def fib_re(n):
    if n < 2:
        return n
    else:
        return fib_re(n-1) + fib_re(n-2)
    # 递归实现fib(100)时间太长，我出去打个电话都没运算完，而动态规划fib(100)秒算

# 动态规划实现
def fib_DP(n):
    results = list(range(n+1))
    for i in range(n+1):
        if i < 2:
            results[i] = i
        else:
            results[i] = results[i-1] + results[i-2]
    return results[n]


if __name__ == '__main__':
    result = fib_DP(100)
    print(result)