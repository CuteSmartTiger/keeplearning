import request from './request';


export const createChange = data => request.post('change', data);
export const listChange = data => request.get('change', data);
export const operateChange = data => request.put('change', data);
export const addChangeComment = data => request.post('change/comment', data);
export const uploadChange = data => request.post('change/upload', data);
export const deleteFileChange = data => request.put('change/upload', data);
export const changeTodos = data => request.get('change/todo', data);

