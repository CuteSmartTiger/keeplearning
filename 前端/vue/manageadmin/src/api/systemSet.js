import axios from '@/libs/api.request'
export const getbackground = (res) => {
  const data = res;
  return axios.request({
    url: '/v2/display/',
    data,
    method: 'post'
  })
}
