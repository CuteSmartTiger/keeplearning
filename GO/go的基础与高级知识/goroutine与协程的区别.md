轻量级线程 可以同时开一千多个
非抢占多任务处理，由协程主动交出控制权
编译器/解释器/虚拟机层面的多任务
多个协程可能在一个或者多个线程上运行 ，go语言调度器调度协程



#### 编写代码说明 非抢占多任务处理，由协程主动交出控制权
线程是抢占式多任务处理





#### 以下情况会陷入死循环，不会交出控制权

```golang
func main() {
	var a [10]int
	for i := 0; i < 10; i++ {
		go func(i int) {
			for {
				a[i]++  //非IO操作，会循环死机
				//runtime.Gosched() //手动交出控制权
			}
		}(i)
	}
	//time.Sleep(time.Minute)
	time.Sleep(time.Millisecond)
	fmt.Println(a)

```



#### 什么情况下才会交出控制权




#### 以下代码中的为什么要传入参数i，以下代码通过go run -race 发现依然有读写错误  需要使用channel处理

```golang
func main() {
	var a [10]int
	for i := 0; i < 10; i++ {
		go func(i int) {
			for {
				a[i]++  //非IO操作，会循环死机
				runtime.Gosched() //手动交出控制权
			}
		}(i)
	}
	//time.Sleep(time.Minute)
	time.Sleep(time.Millisecond)
	fmt.Println(a) //当go func函数不传入i参数时，当i==10时，跳出循环，此处打印会出现超出索引的异常
```
