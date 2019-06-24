import request from './request';


export const listSystem = data => request.get('system', data);
export const addSystem = data => request.post('system', data);
export const updateSystem = data => request.put('system', data);

