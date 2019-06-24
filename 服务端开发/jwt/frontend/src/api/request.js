import axios from 'axios';
import store from '@/store';

function checkStatus(err) {
  if (err.response.status === 404) {
    store.dispatch('showSnackBar', {text: '资源不存在', level: 'error'});
  } else if (err.response.status === 403) {
    store.dispatch('showSnackBar', {text: '您没有该项权限', level: 'error'});
  } else if (err.response.status === 500) {
    store.dispatch('showSnackBar', {text: '服务器发生了点意外', level: 'error'});
  } else {
    store.dispatch('showSnackBar', {text: `${err.response.data.msg}`, level: 'error'});
  }
  return err.response;
}

function checkCode(res) {
  if ((res.status >= 200 && res.status < 400) && (res.data.status === '0' || res.data.status === 0)) {
    return res;
  }
  store.dispatch('showSnackBar', {text: `${res.data.msg}`, level: 'error'});
  return res;

}


export default {
  get(url, params) {
    return axios.get(
      url,
      params,
    ).then(checkCode).catch(checkStatus);
  },
  post(url, data) {
    return axios.post(
      url,
      data,
    ).then(checkCode).catch(checkStatus);
  },
  put(url, data) {
    return axios.put(
      url,
      data,
    ).then(checkCode).catch(checkStatus);
  },
  patch(url, data) {
    return axios.patch(
      url,
      data,
    ).then(checkCode).catch(checkStatus);
  },
  delete(url, data) {
    return axios.delete(
      url,
      data,
    ).then(checkCode).catch(checkStatus);
  },
};

