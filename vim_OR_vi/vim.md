已测试确定内容
####






用vim写代码时，经常遇到这样的场景，复制多行，然后粘贴。
 这样做：
1. 将光标移动到要复制的文本开始的地方，按v进入可视模式。
2. 将光标移动到要复制的文本的结束的地方，按y复制。此时vim会自动将光标定位到选中文本的开始的地方，并退出可视模式。
3. 我移动光标到文本结束的地方，按p粘贴。

一、多行
dd
删除一行
ndd
删除以当前行开始的n行
dw
删除以当前字符开始的一个字符
ndw
删除以当前字符开始的n个字符
d$、D
删除以当前字符开始的一行字符
d)
删除到下一句的开始
d}
删除到下一段的开始
d回车
删除2行

二、复制多行
任务：将第9行至第15行的数据，复制到第16行

方法1：（强烈推荐）
：9，15 copy 16  或 ：9，15 co 16
由此可有：
：9，15 move 16  或 :9,15 m 16 将第9行到第15行的文本内容到第16行的后面  

方法2：
光标移动到结束行，ma
光标移动到起始行,输入y'a
光标移动到需要复制的行，输入p,行前复制则输入大写P

方法3：
把光标移到第9行 shift + v
再把光标移动到第15行  ctrl + c
再把光标死去到第16行  p mysql

方法4：
光标移动到起始行，输入ma
光标移动到结束行，输入mb
光标移动到粘贴行，输入mc
然后输入:'a,'b, co 'c   把co换成m就是剪切
若要删除多行，则输入：'a,'b de

vi设置自动缩进：set smartindent
vi设置显示行号：set number 或 set nu
Vim中如何全选并复制
全部删除：按esc后，然后dG
全部复制：按esc后，然后ggyG
全选高亮显示：按esc后，然后ggvG或者ggVG

vim如何与剪贴板交互（将vim的内容复制出来）

习惯了在windows环境各个应用程序之间如UltraEdit，记事本，eclipse之间ctrl+c,ctrl+v进行复制粘贴的你，如何在vim与别的windows应用程序之间拷贝粘贴呢？
当然你可以在vim里选择用鼠标，选中一块文字然后右键复制，再到应用程序里ctrl+v粘贴，只不过这样效率就差多了。
更好的做法是，在vim中使用 "*y 使用进行复制，然后在应用程序中用ctrl+v粘贴。
从应用程序到vim则在应用程序中使用ctrl+c复制，在vim中使用shift+insert粘贴。

如：

"*yy复制一行
"*y2w复制二个词
……

实现的原理是：
"   表示使用寄存器
"*   表示使用当前选择区
我个人推荐使用ctrl+insert复制，shift+insert粘贴。

vim有多个剪贴板，其中就包括了系统剪贴板。使用命令:reg可以看到各个剪贴板的内容。其中“”表示当前使用的剪贴板，“0-9是历史剪贴板，“#就是系统剪贴板了（你可以在系统里拷贝一些东西，看是不是会出现在“#剪贴板里）。在vim中使用y可以把内容拷贝到“”号剪贴板，继续y会把新的东西放入“”，而原来“”的东西就会被压入“0-9的各个历史剪贴板中。X11系统下还有一个“*的剪贴板对应中键拷贝粘贴，windows不知道有没有。

解决第一个问题：

“+y 把选中内容拷贝到”+号剪贴板，即系统剪贴板

“+p 把系统剪贴板的内容粘贴到vim，这一个用shift+insert也可完成

解决第二个问题：

“0p 可以把已经被挤到”0剪贴板的内容A重新粘贴出来

嫌长的做一个map，映射到某个功能键或组合就方便了。
