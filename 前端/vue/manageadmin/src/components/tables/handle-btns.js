const btns = {
  delete: (h, params, vm) => {
    let disabled = false;
     if(params.tableData[params.index]._disabled){
       disabled = params.tableData[params.index]._disabled
     }
    return h('Poptip', {
      props: {
        confirm: true,
        placement:'left',
        title: '你确定要删除吗?'
      },
      style: {textAlign:'left'},
      on: {
        'on-ok': () => {
          vm.$emit('on-delete', params)
        }
      }
    }, [

      h('Button', {
        props: {
          icon: 'md-trash',
          disabled: disabled,
          ghost: true
        },
        style: {
          marginRight: '5px',
          color: '#666',
        },
      }, '删除')

    ])
  },
  delete2: (h, params, vm) => {
    let disabled = false;
    let undo = params.tableData[params.index].isDelete;
    if(params.tableData[params.index]._disabled){
      disabled = params.tableData[params.index]._disabled
    }
    if(undo){
      return h('Poptip', {
        props: {
          confirm: true,
          placement:'left',
          okText:'是',
          cancelText:'否',
          transfer:true,
          title: '你确定要撤销删除吗?'
        },
        on: {
          'on-ok': () => {
            vm.$emit('on-undo', params)
          }
        }
      }, [
        h('Button', {
          props: {
            icon: 'ios-undo',
            ghost: true
          },
          style: {
            marginRight: '5px',
            color: '#666',
          },
        }, '撤销删除') ])
    }else{
      return h('Poptip', {
        props: {
          confirm: true,
          placement:'left',
          okText:'永久删除',
          cancelText:'临时删除',
          transfer:true,
          title: '你确定要删除吗?'
        },
        on: {
          'on-ok': () => {
            params['isDelete'] = false;
            vm.$emit('on-delete', params)
          },
          'on-cancel': () => {
            params['isDelete'] = true;
            vm.$emit('on-delete', params)
          }
        }
      }, [
        h('Button', {
          props: {
            icon: 'md-trash',
            disabled: disabled,
            ghost: true
          },
          style: {
            marginRight: '5px',
            color: '#666',
          },
        }, '删除') ])

    }
  },
  edit: (h, params, vm) => {
    let disabled = false;
    return h('Button', {
      props: {
        icon: 'md-create',
        disabled: disabled,
        ghost: true
      },
      style: {
        marginRight: '5px',
        color: '#2d8cf0',
      },
      on: {
        click: () => {
          vm.$emit('on-edit', params)
        }
      }
    }, '修改')
  }
}

export default btns
