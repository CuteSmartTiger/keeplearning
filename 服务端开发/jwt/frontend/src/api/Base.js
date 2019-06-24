import request from './request';


export const getJWT = data => request.post('login', data);
export const listTenant = data => request.get('tenant', data);

