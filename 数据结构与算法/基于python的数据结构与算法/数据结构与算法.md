### 算法篇

#### 排序

#### 查找
- 二分查找

   使用对象：以有序表表示静态查找表时，查找函数可以用二分查找来实现。

- 思路：

   二分查找（Binary Search）的查找过程是：先确定待查记录所在的区间，然后逐步缩小区间直到找到或找不到该记录为止。
1. 二分查找的时间复杂度是O(log(n))，最坏情况下的时间复杂度是O(n)。
2. 假设 low 指向区间下界，high 指向区间上界，mid 指向区间的中间位置，则 mid  = （low + high) / 2,具体过程：
  1.先将关键字与 mid 指向的元素比较，如果相等则返回mid。
  2.关键字小于 mid 指向的元素关键字，则在 [ low,  mid-1 ]区间中继续进行二分查找。
  3.关键字大于mid 指向的元素关键字，则在[ mid +1 , high] 区间中继续进行二分查找。
- 实现代码
```python
#!/usr/bin/env python
# python2.7
import sys
def search2(a,m):
  low = 0
  high = len(a) - 1
  while(low <= high):
    mid = low/2 + high/2
    midval = a[mid]
    if midval < m:
      low = mid + 1
    elif midval > m:
      high = mid - 1
    else:
      print mid
      return mid
  print -1
  return -1
if __name__ == "__main__":
  a = [int(i) for i in list(sys.argv[1])]
  m = int(sys.argv[2])
  search2(a,m)
```
