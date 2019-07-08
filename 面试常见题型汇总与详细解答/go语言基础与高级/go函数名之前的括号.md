#### 理解之前需要理解的概念
1. go中如何面向对象的
2. go中函数与方法的定义与区别
3. 指针作为接收者与值作为接受者的区别


```GO
// 代码学习

package engine

import (
	"log"
	"2.1concurrencespider/fetcher"
)

type SimpleEngine struct {}


func (e SimpleEngine) Run(seeds ...Request) {
	var requests []Request
	for _, r := range seeds {
		//log.Printf("seeds is %v",r)
		requests = append(requests, r)
	}
	for len(requests) > 0 {
		r := requests[0]
		requests = requests[1:]
		//log.Printf("Fetching %s", r.Url)
		parseResult,err := e.worker(r)
		if err!=nil{
			continue
		}
		//将解析获得结果继续添加到requests队列中
		requests = append(requests, parseResult.Requests...)

		for _, item := range parseResult.Items {
			log.Printf("Got item %v", item)
		}
	}
}


//定义一个worker函数，其功能包含engine parse fetcher
func (SimpleEngine) worker(r Request) (ParseResult, error) {
	log.Printf("Fetching %s", r.Url)
	body, err := fetcher.Fetch(r.Url)
	if err != nil {
		log.Printf("Fetcher: err"+"fetching url %s:%v", r.Url, err)
		return ParseResult{}, err
	}
	return r.ParserFunc(body),nil


```
