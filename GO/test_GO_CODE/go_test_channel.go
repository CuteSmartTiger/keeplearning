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

