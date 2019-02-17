import axios from '@/libs/api.request'
export const getDatas = (res) => {
  let type = res.type;
  switch (type){
    case 0:
      return axios.request({
        url: '/v2/hostparams/' + res.id,
        params: res,
        method: 'get'
      })
    break;
    case 1:
      return axios.request({
        url: '/v2/virtualmachineparams/' + res.id,
        params: res,
        method: 'get'
      })
      break;
    default:
      return axios.request({
        url: '/v2/virtualmachineparams/' + res.id,
        params: res,
        method: 'get'
      })
      break
  }

}
export const getIndexparams = () => {
  return axios.request({
    url: '/v2/indexparams',
    method: 'get'
  })
}

export const getXenServerHostData = (res) => {
  return axios.request({
    url: '/v2/xenserverhost',
    params: res,
    method: 'get'
  })
}
