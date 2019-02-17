import env from './env'
const DEV_URL = ''
const PRO_URL = '';
export default env === 'development' ? DEV_URL : PRO_URL
