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
