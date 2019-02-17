Vuex 是一个专为 Vue.js 设计的状态管理模式


vuex解决了组件之间同一状态的共享问题。当我们的应用遇到多个组件共享状态时，会需要：

多个组件依赖于同一状态。传参的方法对于多层嵌套的组件将会非常繁琐，并且对于兄弟组件间的状态传递无能为力。这需要你去学习下，vue编码中多个组件之间的通讯的做法。
来自不同组件的行为需要变更同一状态。我们经常会采用父子组件直接引用或者通过事件来变更和同步状态的多份拷贝。

以上的这些模式非常脆弱，通常会导致无法维护的代码。来自官网的一句话：Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。

它采用集中式存储管理应用的所有组件的状态。这里的关键在于集中式存储管理。这意味着本来需要共享状态的更新是需要组件之间通讯的，而现在有了vuex，就组件就都和store通讯了。问题就自然解决了。

这就是为什么官网再次会提到Vuex构建大型应用的价值。如果您不打算开发大型单页应用，使用 Vuex 可能是繁琐冗余的。确实是如此——如果您的应用够简单，您最好不要使用 Vuex。







Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式


    1.vuex解决了组件之间同一状态的共享问题  （解决了不同组件之间的数据共享）

    2.组件里面数据的持久化。                



小项目不部建议用vuex   









vuex的使用：




	1、src目录下面新建一个vuex的文件夹



	2、vuex 文件夹里面新建一个store.js


	3、安装vuex  

		cnpm install vuex --save

	4、在刚才创建的store.js引入vue  引入vuex 并且use vuex

		import Vue from 'vue'
		import Vuex from 'vuex'

		Vue.use(Vuex)



	5、定义数据

			/*1.state在vuex中用于存储数据*/
			var state={

			    count:1
			}


	6、定义方法	 mutations里面放的是方法，方法主要用于改变state里面的数据

		var mutations={

		    incCount(){

			++state.count;
		    }
		}


	7、优点类似计算属性   ，  改变state里面的count数据的时候会触发 getters里面的方法 获取新的值 (基本用不到)


		var getters= {

		    computedCount: (state) => {
			return state.count*2
		    }
		}



	8、 Action 基本没有用

		Action 类似于 mutation，不同在于：

		Action 提交的是 mutation，而不是直接变更状态。
		Action 可以包含任意异步操作。



		var actions= {
		    incMutationsCount(context) {    /*因此你可以调用 context.commit 提交一个 mutation*/


			context.commit('incCount');    /*执行 mutations 里面的incCount方法 改变state里面的数据*/


		    }
		}




	暴露

		const store = new Vuex.Store({
		    state,
		    mutations,
		    getters,
		    actions
		})



		export default store;






组建里面使用vuex：


		1.引入 store

			 import store from '../vuex/store.js';


		2、注册

			 export default{
				data(){
				    return {               
				       msg:'我是一个home组件',
					value1: null,

				    }
				},
				store,
				methods:{
				    incCount(){

					this.$store.commit('incCount');   /*触发 state里面的数据*/
				    }

				}
			    }
		3、获取state里面的数据  

			this.$store.state.数据



		4、触发 mutations 改变 state里面的数据

			this.$store.commit('incCount');


		5、触发 actions里面的方法

			this.$store.dispatch('incCount');


		6、{{this.$store.getters.computedCount}}  获取 getters里面方法返回的的数据
		
