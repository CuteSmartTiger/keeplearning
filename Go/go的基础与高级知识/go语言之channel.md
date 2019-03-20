- [channnel定义、发送、接受信息](#first)
- [单向通道](#unidirectional)
<h5 id="first">channnel定义、发送、接受信息</h5>
```go
package main

import (
	"fmt"
)

func main() {
	ch := make(chan string)
	go func(){
		// 在执行到这一步的时候main goroutine才会停止阻塞
		str := <- ch
		fmt.Println("receive data：" + str)
	}()
	ch <- "hello"
	fmt.Println("channel has send data")
}
// goroutine向channel发送数据的时候如果缓冲还没满，那么该goroutine就不会阻塞
```


<h5 id="unidirectional">单向通道</h5>

```go
package main
import (
	"fmt"
	"time"
)

func main(){
	ch := make(chan string)

	go func(out chan <- string){
		out <- "hello"
	}(ch)

	go func(in <- chan string){
		te := <- in
		fmt.Println(te)
	}(ch)

	time.Sleep(2 * time.Second)
}
```
