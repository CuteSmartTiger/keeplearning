import axios from '@/libs/api.request'

export const getTableData = () => {
  return axios.request({
    url: 'get_table_data',
    method: 'get'
  })
}
export const getPoliciesData = (res) => {
  return axios.request({
    url: '/v2/policies',
    params: res,
    method: 'get'
  })
}
export const getPoliciesInfo = (id) => {
  return axios.request({
    url: '/v2/policies/' + id,
    method: 'get'
  })
}
export const deletePolicies = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/policies/',
    data,
    method: 'delete'
  })
}
export const editPolicies = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/policies/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/policies/',
      data,
      method: 'post'
    })
  }
}
