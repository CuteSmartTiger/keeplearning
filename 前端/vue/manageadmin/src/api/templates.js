import axios from '@/libs/api.request'
export const getTemplatesData = (res) => {
  return axios.request({
    url: '/v2/templates',
    params: res,
    method: 'get'
  })
}
export const detailTemplatesData = (id) => {
  return axios.request({
    url: '/v2/templates/' + id,
    method: 'get'
  })
}
export const deleteTemplatesData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/templates/',
    data,
    method: 'delete'
  })
}
export const editTemplatesData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/templates/clone/' + data.id ,
      data,
      method: 'post'
    })
  }else{
    return axios.request({
      url: '/v2/templates/clone/',
      data,
      method: 'post'
    })
  }
}
