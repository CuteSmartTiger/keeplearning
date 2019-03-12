go语言中找&和*区别



指针，或者说pointer是一串指向某个内存地址的字符串，所谓指向是指这串字符串的内容是内存地址的值

&表示取地址，例如你有一个变量a那么&a就是变量a在内存中的地址，对于golang，指针也是有类型的，比如如果a是一个string那么&a是一个string的指针类型，在go里面叫&string

所以你看到b := &a，a，b是两个不同的变量，a是string类型，b是&string类型，你用fmt去打印b，你会发现它是一串内存地址，而非a的值

所以为了拿到a的值，有个操作*，用来取出指针对应内存地址里存的值，所以当你fmt打印一下*b它会跟a一模一样

a := "123"
b := &a
fmt.Println(a)
fmt.Println(b)
fmt.Println(*b)
