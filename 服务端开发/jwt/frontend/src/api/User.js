import request from './request';


export const listUser = data => request.get('user', data);
export const updateUser = data => request.put('user', data);

