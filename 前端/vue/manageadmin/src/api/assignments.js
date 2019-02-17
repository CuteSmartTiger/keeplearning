import axios from '@/libs/api.request'
export const getAssignmentsData = (res) => {
  return axios.request({
    url: '/v2/assignments',
    params: res,
    method: 'get'
  })
}
export const detailAssignmentsData = (id) => {
  return axios.request({
    url: '/v2/assignments/' + id,
    method: 'get'
  })
}
export const deleteAssignmentsData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/assignments/',
    data,
    method: 'delete'
  })
}
export const undoAssignmentsData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/assignments/',
    data,
    method: 'put'
  })
}
export const editAssignmentsData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/assignments/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/assignments/',
      data,
      method: 'post'
    })
  }
}
export const TreeOwner = (res) => {
  if(res.id){
    return axios.request({
      url: '/v2/assignments/owners/'+res.id,
      method: 'get'
    })
  }else{
    return axios.request({
      url: '/v2/assignments/owners',
      params: res,
      method: 'get'
    })
  }

}
export const TreeMachines = (res) => {
  if (res.id) {
    return axios.request({
      url: '/v2/assignments/machines/' + res.id,
      method: 'get'
    })
  } else {
    return axios.request({
      url: '/v2/assignments/machines',
      params: res,
      method: 'get'
    })
  }
}
export const TreeLDAPOwner = (res) => {
  if(res.id){
    return axios.request({
      url: '/v2/assignments/ldapobjects/'+res.id,
      method: 'get'
    })
  }else{
    return axios.request({
      url: '/v2/assignments/ldapobjects',
      method: 'get'
    })
  }
}

export const searchTree = (res) => {
  return axios.request({
    url: '/v2/assignments/searchtree',
    params: res,
    method: 'get'
  })
}
