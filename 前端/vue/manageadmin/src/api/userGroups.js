import axios from '@/libs/api.request'
export const getGroupsData = (res) => {
  return axios.request({
    url: '/v2/groups',
    params: res,
    method: 'get'
  })
}
export const getGroupsInfo = (id) => {
  return axios.request({
    url: '/v2/groups/' + id,
    method: 'get'
  })
}
export const deleteGroupsData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/groups/',
    data,
    method: 'delete'
  })
}
export const editGroupsData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/groups/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/groups/',
      data,
      method: 'post'
    })
  }
}
