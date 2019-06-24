import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);


const LOGIN = 'LOGIN';
const LOGOUT = 'LOGOUT';
const SHOW_SNACKBAR = 'SHOW_SNACKBAR';
const DISMISS_SNACKBAR = 'DISMISS_SNACKBAR';

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    username: localStorage.getItem('username'),
    tenant: localStorage.getItem('tenant'),
    isLoggedIn: !!localStorage.getItem('token'),
    snackBar: {text: '', level: '', value: false},
  },
  mutations: {
    [LOGIN](state) {
      state.isLoggedIn = true;
    },
    [LOGOUT](state) {
      state.isLoggedIn = false;
    },
    [SHOW_SNACKBAR](state, {text, level}) {
      state.snackBar = {text, level, value: true};
    },
    [DISMISS_SNACKBAR](state) {
      state.snackBar = {text: '', level: '', value: false};
    },
  },
  actions: {
    login({commit}, payload) {
      localStorage.setItem('token', payload.token);
      localStorage.setItem('username', payload.username);
      localStorage.setItem('tenant', payload.tenant);
      commit(LOGIN);
    },
    logout({commit}) {
      localStorage.clear();
      commit(LOGOUT);
    },
    showSnackBar({commit}, payload) {
      commit(SHOW_SNACKBAR, payload);
    },
    dismissSnackBar({commit}) {
      commit(DISMISS_SNACKBAR);
    },
  },
  getters: {
    isLoggedIn(state) {
      return state.isLoggedIn;
    },
    username(state) {
      return state.username;
    },
    tenant(state) {
      return state.tenant;
    },
  },
});

export default store;
