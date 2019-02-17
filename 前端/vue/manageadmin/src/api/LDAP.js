import axios from '@/libs/api.request'
export const getldapserversData = (res) => {
  return axios.request({
    url: '/v2/ldapservers',
    params: res,
    method: 'get'
  })
}
export const detailldapserversData = (id) => {
  return axios.request({
    url: '/v2/ldapservers/' + id,
    method: 'get'
  })
}
export const deleteldapserversData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/ldapservers/',
    data,
    method: 'delete'
  })
}
export const editldapserversData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/ldapservers/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/ldapservers/',
      data,
      method: 'post'
    })
  }
}
export const testldapserversData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/ldapservers/test',
    data,
    method: 'post'
  })
}
