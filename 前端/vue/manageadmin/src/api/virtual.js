import axios from '@/libs/api.request'
export const getVirtualData = (res) => {
  return axios.request({
    url: '/v2/hostservers',
    params: res,
    method: 'get'
  })
}
export const detailVirtualData = (id) => {
  return axios.request({
    url: '/v2/hostservers/' + id,
    method: 'get'
  })
}
export const deleteVirtualData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/hostservers/',
    data,
    method: 'delete'
  })
}
export const editVirtualData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/hostservers/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/hostservers/',
      data,
      method: 'post'
    })
  }
}
export const testVirtualData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/hostservers/test',
    data,
    method: 'post'
  })
}
