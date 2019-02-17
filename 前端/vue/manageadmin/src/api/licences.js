import axios from '@/libs/api.request'
export const getLicensesData = (res) => {
  return axios.request({
    url: '/v2/license',
    params: res,
    method: 'get'
  })
}
export const postLicensesData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/license/finger/',
    data,
    method: 'post'
  })
}
export const fileLicensesData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/license/allowed/',
    data,
    method: 'post'
  })
}
