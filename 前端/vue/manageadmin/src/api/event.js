import axios from '@/libs/api.request'
export const getEventData = (res) => {
  return axios.request({
    url: '/v2/events',
    params: res,
    method: 'get'
  })
}
export const detailEventData = (id) => {
  return axios.request({
    url: '/v2/events/' + id,
    method: 'get'
  })
}
export const deleteEventData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/events/',
    data,
    method: 'delete'
  })
}
export const editEventData = (res) => {
  const data = res;
  if(data.id != undefined){
    return axios.request({
      url: '/v2/events/' + data.id ,
      data,
      method: 'put'
    })
  }else{
    return axios.request({
      url: '/v2/events/',
      data,
      method: 'post'
    })
  }
}
export const testEventData = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/events/test',
    data,
    method: 'post'
  })
}
