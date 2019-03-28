package main

import "fmt"

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // 把 sum 发送到通道 c
}

func main() {
	s := []int{7, 2, 8, -9, 4, 0,5,-60,9}

	c := make(chan int,8)
	//go sum(s[:len(s)/2], c)
	go sum(s[:2], c)
	//go sum(s[len(s)/2:], c)
	go sum(s[2:5], c)
	go sum(s[5:], c)
	x, y ,z:= <-c, <-c ,<-c// 从通道 c 中接收

	fmt.Println(x, y, z)
}

