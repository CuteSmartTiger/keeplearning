
export const getRules = (rulesName) => {
  let rules = {
    name: [
      { required: true, message: '名称不能为空', trigger: 'blur' },
      { type: 'string', min: 4, max: 20, message: '名称在4-20字符之间', trigger: 'change' }
    ],
    username: [
      { required: true, message: '用户名不能为空', trigger: 'blur' },
      { type: 'string', min: 4, max: 20, message: '用户名在4-20字符之间', trigger: 'change' }
    ],
    password: [
      { required: true, message: '密码不能为空', trigger: 'blur' },
      { type: 'string', min: 6, max:16, message: '密码在6-16字符之间', trigger: 'blur' }
    ],
    password2: [
      { type: 'string', min: 6, max:16, message: '密码在6-16字符之间', trigger: 'blur' }
    ],
    count: [
      { type: 'number',required: true, message: '数量不能为空', trigger: 'blur' }
    ],
    user_dn: [
      { required: true, message: '用户可区分名称', trigger: 'blur' }
    ],
    hostname: [
      { required: true, message: '主机名称不能为空', trigger: 'blur' }
    ],
    file_location: [
      { required: true, message: '文件存储位置不能为空', trigger: 'blur' }
    ],
    ip1: [
      { type: 'number',required: true, message: '不能为空', trigger: 'blur' }
    ],
    netmask1: [
      { type: 'number',required:true, message:'不能为空',trigger: 'blur'}
    ],
    gateway1: [
      { type: 'number',required:true, message:'不能为空',trigger: 'blur'}
    ],
  }

  const ruleRes = {};
  rulesName.forEach((item)=>{
    if(rules[item] != undefined){
      ruleRes[item] = rules[item];
    }
  })
  return ruleRes;
}
