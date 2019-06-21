import axios from 'axios';

// read base url from window location
if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = 'http://localhost:8000/api/v1';
  // axios.defaults.baseURL = 'http://10.12.128.252:9110/api/v1/';
} else {
  axios.defaults.baseURL = `${window.location.origin}/api/v1`;
}


export * from './Base';
export * from './User';
export * from './System';
export * from './Deploy';
export * from './Change';
