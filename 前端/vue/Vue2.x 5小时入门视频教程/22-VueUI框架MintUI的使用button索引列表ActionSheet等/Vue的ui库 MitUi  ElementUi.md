基于Vue的Ui框架


	饿了么公司基于vue开的的vue的Ui组件库


		Element Ui    基于vue  pc端的UI框架  


		MintUi         基于vue 移动端的ui框架






http://element.eleme.io/




http://mint-ui.github.io/#!/en




mintUI的使用：



	1.找官网

	2.安装   npm install mint-ui -S         -S表示  --save

	3.引入mint Ui的css 和 插件

		import Mint from 'mint-ui';

		Vue.use(Mint);


		import 'mint-ui/lib/style.css'


	4.看文档直接使用。




在mintUi组件上面执行事件的写法

@click.native



<mt-button @click.native="sheetVisible = true" size="large">点击上拉 action sheet</mt-button>
