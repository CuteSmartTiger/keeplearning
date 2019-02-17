import axios from '@/libs/api.request'
export const getLdapObjData = (res) => {
  return axios.request({
    url: '/v2/ldapobjects',
    params: res,
    method: 'get'
  })
}
export const detailLdapObjData = (id) => {
  return axios.request({
    url: '/v2/ldapobjects/' + id,
    method: 'get'
  })
}
export const deleteLdapObjData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/ldapobjects/',
    data,
    method: 'delete'
  })
}
export const editLdapObjData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/ldapobjects/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/ldapobjects/',
      data,
      method: 'post'
    })
  }
}
export const testLdapObjData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/ldapobjects/test',
    data,
    method: 'post'
  })
}
