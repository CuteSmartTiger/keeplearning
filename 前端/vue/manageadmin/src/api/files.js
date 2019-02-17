import axios from '@/libs/api.request'
export const getFilesData = (res) => {
  return axios.request({
    url: '/v2/packages',
    params: res,
    method: 'get'
  })
}
export const detailFilesData = (id) => {
  return axios.request({
    url: '/v2/packages/' + id,
    method: 'get'
  })
}
export const deleteFilesData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/packages/',
    data,
    method: 'delete'
  })
}
export const editFilesData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/packages/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/packages/',
      data,
      method: 'post'
    })
  }
}
export const testFilesData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/packages/test',
    data,
    method: 'post'
  })
}
