import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);


/*1.state在vuex中用于存储数据*/
var state={

    count:1,
    list:[]
}

/*2.mutations里面放的是方法，方法主要用于改变state里面的数据
*/
var mutations={

    incCount(){

        ++state.count;
    },
    addList(state,data){

        state.list = data;
    }
}

/*3、优点类似计算属性   ，  改变state里面的count数据的时候会触发 getters里面的方法 获取新的值 (基本用不到)*/


var getters= {
   
    computedCount: (state) => {
        return state.count*2
    }
}



/*
4、 基本没有用

Action 类似于 mutation，不同在于：

Action 提交的是 mutation，而不是直接变更状态。
Action 可以包含任意异步操作。
*/


var actions= {
    incMutationsCount(context) {    /*因此你可以调用 context.commit 提交一个 mutation*/
      
      
        context.commit('incCount');    /*执行 mutations 里面的incCount方法 改变state里面的数据*/


    }
}



//vuex  实例化 Vuex.store   注意暴露
const store = new Vuex.Store({
    state,
    mutations,
    getters,
    actions
})


export default store;

