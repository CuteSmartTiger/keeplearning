import request from './request';


export const createDeploy = data => request.post('deploy', data);
export const listDeploy = data => request.get('deploy', data);
export const operateDeploy = data => request.put('deploy', data);
export const addComment = data => request.post('deploy/comment', data);
export const uploadDeploy = data => request.post('deploy/upload', data);
export const deleteFileDeploy = data => request.put('deploy/upload', data);
export const deployTodos = data => request.get('deploy/todo', data);

