- 类型：交换排序
- 应用场景：
- 时间复杂度：平均O(n2)
- 空间复杂度：O(1)
- 稳定性:稳定
- 代码：
  ```Python
  def bubble_sort(target_list):
      '''基于Python的bubble sort'''
      for i in range(len(target_list) - 1):
          flag = False  # 标记此趟比较是否发生交换
          for j in range(len(target_list) - i - 1):
              if target_list[j] > target_list[j + 1]:
                  target_list[j], target_list[j + 1] = target_list[j + 1], target_list[i]
                  flag = True

          # 优化：某一趟未发生交换时，跳出循环
          if not flag:
              # print('i== %d,break' % i)
              break
      return target_list

  ```

  ```go
  package main //必须有个main包

  import "fmt"
  import "math/rand"
  import "time"

  
  //  基于go语言的冒泡排序
  func main() {
  	//设置种子， 只需一次
  	rand.Seed(time.Now().UnixNano())

  	var a [10]int
  	n := len(a)

  	for i := 0; i < n; i++ {
  		a[i] = rand.Intn(100) //100以内的随机数
  		fmt.Printf("%d, ", a[i])
  	}
  	fmt.Printf("\n")

  	var flag bool
  	//冒泡排序，挨着的2个元素比较，升序（大于则交换）
  	for i := 0; i < n-1; i++ {
  		flag = false
  		for j := 0; j < n-1-i; j++ {
  			if a[j] > a[j+1] {
  				a[j], a[j+1] = a[j+1], a[j]
  				flag = true
  			}
  		}
  		if flag == false{
  			break
  		}

  	}

  	fmt.Printf("\n排序后:\n")
  	for i := 0; i < n; i++ {
  		fmt.Printf("%d, ", a[i])
  	}
  	fmt.Printf("\n")

  }
  ```
