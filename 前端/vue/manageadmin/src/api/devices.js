import axios from '@/libs/api.request'
export const getDeviceData = (res) => {
  return axios.request({
    url: '/v2/devicemanagers',
    params: res,
    method: 'get'
  })
}
export const detailDeviceData = (id) => {
  return axios.request({
    url: '/v2/devicemanagers/' + id,
    method: 'get'
  })
}
export const deleteDeviceData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/devicemanagers/',
    data,
    method: 'delete'
  })
}
export const editDeviceData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/devicemanagers/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/devicemanagers/',
      data,
      method: 'post'
    })
  }
}
export const testDeviceData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/devicemanagers/test',
    data,
    method: 'post'
  })
}
