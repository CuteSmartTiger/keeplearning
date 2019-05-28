# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
# f(n)=f(n-1)+f(n-2)
def fb(n):
    assert n > 0, "n must > 0"
    return n if n in (1, 2) else fb(n - 1) + fb(n - 2)


print(fb(3))
print(fb(2))
print(fb(5))


def fib(n):
    a, b = 1, 0
    cout = 0
    while cout < n:
        a, b = a + b, a
        cout += 1
    return a


print(fib(3))
print(fib(2))
print(fib(5))
