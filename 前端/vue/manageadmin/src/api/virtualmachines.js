import axios from '@/libs/api.request'
export const getVirtualmachinesData = (res) => {
  return axios.request({
    url: '/v2/virtualmachines',
    params: res,
    method: 'get'
  })
}
export const detailVirtualmachinesData = (id) => {
  return axios.request({
    url: '/v2/virtualmachines/' + id,
    method: 'get'
  })
}
// export const deleteVirtualmachinesData = (res) => {
//   const data = res;
//   return axios.request({
//     url: '/v2/virtualmachines/',
//     data,
//     method: 'delete'
//   })
// }
export const editVirtualmachinesData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/virtualmachines/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/virtualmachines/',
      data,
      method: 'post'
    })
  }
}
export const pushPackage = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/virtualmachines/push_package/',
    data,
    method: 'post'
  })
}
export const pushUserfile = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/virtualmachines/push_userfile/',
    data,
    method: 'post'
  })
}
export const getLog = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/virtualmachines/logs',
    data,
    method: 'post'
  })
}
export const modifyVirtualmachines = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/virtualmachines/',
    data,
    method: 'put'
  })
}

