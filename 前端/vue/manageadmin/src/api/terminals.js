import axios from '@/libs/api.request'
export const getTerminalsData = (res) => {
  return axios.request({
    url: '/v2/terminals',
    params: res,
    method: 'get'
  })
}
export const detailTerminalsData = (id) => {
  return axios.request({
    url: '/v2/terminals/' + id,
    method: 'get'
  })
}
export const deleteTerminalsData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/terminals/',
    data,
    method: 'delete'
  })
}
export const editTerminalsData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/terminals/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/terminals/',
      data,
      method: 'post'
    })
  }
}
export const pushPackage = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/terminals/push_package/',
    data,
    method: 'post'
  })
}
export const getLog = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/terminals/logs',
    data,
    method: 'post'
  })
}
