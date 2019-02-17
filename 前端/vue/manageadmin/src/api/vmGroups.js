import axios from '@/libs/api.request'
export const getvmGroupsData = (res) => {
  return axios.request({
    url: '/v2/vmgroups',
    params: res,
    method: 'get'
  })
}
export const deletevmGroupsData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/vmgroups/',
    data,
    method: 'delete'
  })
}
export const editvmGroupsData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/vmgroups/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/vmgroups/',
      data,
      method: 'post'
    })
  }
}
