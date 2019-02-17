基于Vue的Ui框架


	饿了么公司基于vue开的的vue的Ui组件库


		Element Ui    基于vue  pc端的UI框架  


		MintUi         基于vue 移动端的ui框架



http://element.eleme.io/


element UI的使用：



	1.找官网  http://element.eleme.io/#/zh-CN/component/quickstart

	2.安装  cnpm i element-ui -S         -S表示  --save

	3.引入element UI的css 和 插件

		import ElementUI from 'element-ui';
		import 'element-ui/lib/theme-chalk/index.css';
		Vue.use(ElementUI);




	4、*webpack.config.js  配置file_loader      http://element.eleme.io/1.4/#/zh-CN/component/quickstart


		  {
			test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
			loader: 'file-loader'
	          }



	5.看文档直接使用。




element UI组件的单独使用（第一种方法）：


	1、cnpm install babel-plugin-component -D    


	2、找到.babelrc 配置文件
		把

		{
		  "presets": [
		    ["env", { "modules": false }],
		    "stage-3"
		  ]
		}


		改为  注意：


		{
		  "presets": [["env", { "modules": false }]],
		  "plugins": [
		    [
		      "component",
		      {
			"libraryName": "element-ui",
			"styleLibraryName": "theme-chalk"
		      }
		    ]
		  ]
		}

	3、
	import { Button, Select } from 'element-ui';

	Vue.use(Button)
	Vue.use(Select)


element UI组件的单独使用（第二种方法）：



	import { Button, Select } from 'element-ui';

	Vue.use(Button)
	Vue.use(Select)


	引入对应的css

		import 'element-ui/lib/theme-chalk/index.css';

	如果报错： webpack.config.js  配置file_loader

		  {
			test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
			loader: 'file-loader'
	          }


	
