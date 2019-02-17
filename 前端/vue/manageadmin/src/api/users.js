import axios from '@/libs/api.request'
export const getUserData = (res) => {
  return axios.request({
    url: '/v2/users',
    params: res,
    method: 'get'
  })
}
export const getUserInfo = (id) => {
  return axios.request({
    url: '/v2/users/' + id,
    method: 'get'
  })
}
export const deleteUserData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/users/',
    data,
    method: 'delete'
  })
}
export const editUserData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/users/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/users/',
      data,
      method: 'post'
    })
  }
}
export const editPasswordData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/users/' + data.id +'/change_password',
    data,
    method: 'post'
  })
}

export const addexcel = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/users/add_users_from_excel',
    data,
    method: 'post'
  })
}
