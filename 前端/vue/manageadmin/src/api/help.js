import axios from '@/libs/api.request'
export const getAboutData = (res) => {
  return axios.request({
    url: '/v2/help',
    params: res,
    method: 'get'
  })
}
export const getLog = (res) => {
  return axios.request({
    url: '/v2/platform/logs',
    method: 'get'
  })
}
