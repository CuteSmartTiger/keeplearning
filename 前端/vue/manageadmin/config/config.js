import env from './env'
const DEV = {
  BASE: '/'
}
const PRO = {
  BASE: '/admin/'
}

export default env === 'development' ? DEV : PRO
