# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# f(n)=f(n-1)+f(n-2)+f(n-3)+………+f(n-(n-2))+f(1) 而又因为f(n-1)=f(n-2)+f(n-3)+………+f(n-(n-2))+f(1)
# 所以f(n)=2f(n-1)
# n=1,f(1)=1
# f(n)=2^n-1

def another_fb(n):
    return n if n == 1 else 2 * another_fb(n - 1)


print(another_fb(3))
