import axios from '@/libs/api.request'
export const getType = (name) => {
  return axios.request({
    url: '/v2/type',
    params: {name: name},
    method: 'get'
  })
}
