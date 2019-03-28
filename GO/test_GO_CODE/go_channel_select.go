package main

import (
	"fmt"
	"time"
)

func main() {
	broadcaster1 := make(chan string) // 频道1
	broadcaster2 := make(chan string) // 频道2

	//broadcaster2 <- "频道二"

	select {
	case mess1 := <-broadcaster1:
		fmt.Println("来自频道1的消息：" + mess1)
	case mess2 := <-broadcaster2:
		fmt.Println("来自频道2的消息：" + mess2)
	default:
		fmt.Println("暂时没有任何频道的消息，请稍后再来~")
		time.Sleep(2 * time.Second)
	}


}