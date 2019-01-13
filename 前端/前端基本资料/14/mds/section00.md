## javascript 对象  

对象是什么，可以先从对象的实现方式去理解，对象就是将一批相关的变量和函数封装在一起的一个整体，这个整体里面的变量叫做属性，函数叫做方法，将它们封装在一起是为了方便程序的编写。方便在哪里？首先可以快速地操作一些属性和方法，不用自己定义，也不用关心方法如何实现，其次可以避免命名冲突。

** 内置对象(已有) **  
```
// 对象上的属性(变量)
var sPi = Math.PI;

// 对象上的方法(函数)
var iNum = Math.floor(5.85);		

alert(sPi);
alert(iNum);
console.log(Math);
```

** 自定义对象 **  
```
//面向对象的方式创建对象
var oMan01 = new Object();
oMan01.name = 'jack';
oMan01.age = 18;
oMan01.talk = function(s){
	alert('我可以说'+s);
}
alert(oMan01.name);
alert(oMan01.age);
oMan01.talk('English');


//对象直接量的方式创建对象
var oMan02 = {
	name:'tom',
	age:16,
	talk:function(s){
		alert('我会说'+s);
	}
}
alert(oMan02.name);
alert(oMan02.age);
oMan02.talk('普通话');

```




 

