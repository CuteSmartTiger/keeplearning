package main

import "fmt"

func TestA() {
	fmt.Println("func TestA()")
}

func TestB() (err error) {
	defer func() { //在发生异常时，设置恢复
		if x := recover(); x != nil {
			//panic value 被附加到错误信息中；
			//并用err 变量接收错误信息，返回给调用者。
			err = fmt.Errorf("internal error: %v", x)
		}
	}()
	panic("func TestB(): panic")
}

func TestC() {
	fmt.Println("func TestC()")
}

func main(){

	defer func() {
		if x:=recover();x !=nil{
			str :="hello"
			fmt.Printf("%s",str)
		}

	}()
	panic("Error")
}

//func main() {
//	TestA()
//	err := TestB()
//	fmt.Println(err)
//	TestC()
//	}