import axios from '@/libs/api.request'

export const login = ({ username, password }) => {
  const data = {
    username,
    password
  }
  return axios.request({
    url: '/v2/login',
    data,
    method: 'post'
  })
}

export const getUserInfo = (token) => {
  return axios.request({
    url: '/v2/assignments',
    method: 'get'
  })
}
export const logout = (token) => {
  return axios.request({
    url: '/v2/logout',
    method: 'get'
  })
}
