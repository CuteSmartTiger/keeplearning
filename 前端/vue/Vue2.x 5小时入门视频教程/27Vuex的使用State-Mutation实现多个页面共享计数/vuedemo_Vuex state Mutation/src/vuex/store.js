import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);


/*1.state在vuex中用于存储数据*/
var state={

    count:1
}

/*2.mutations里面放的是方法，方法主要用于改变state里面的数据
*/
var mutations={

    incCount(){

        ++state.count;
    }
}

//vuex  实例化 Vuex.store
const store = new Vuex.Store({
    state,
    mutations
})


export default store;

