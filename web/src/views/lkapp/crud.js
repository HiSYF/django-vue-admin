import { request } from '@/api/service';
import { BUTTON_STATUS_NUMBER } from '@/config/button';
import { urlPrefix as bookPrefix } from './api';

export const crudOptions = vm => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false
    },
    rowHandle: {
      width: 140,
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve');
        }
      },
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update');
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete');
        }
      }
    },
    indexRow: {
      // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },
    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 24, // 默认的表单 span
      width: '35%'
    },
    columns: [{
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 90,
      form: {
        disabled: true
      }
    }, {
      title: '城市',
      key: 'city',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '城市必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入所属城市'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '粮库名称',
      key: 'lk_name',
      sortable: true,
      treeNode: true,

      type: 'input',
      form: {
        editDisabled: true,
        rules: [
          // 表单校验规则
          { required: true, message: '粮库名称必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入粮库名称'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: 'web端口',
      key: 'server_web_port',
      sortable: true,
      type: 'input',
      form: {
        editDisabled: true,
        rules: [
          // 表单校验规则
          { required: true, message: 'web端口必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入web端口'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: 'ssh端口',
      key: 'server_ssh_port',
      sortable: true,
      type: 'input',
      form: {
        editDisabled: true,
        rules: [
          // 表单校验规则
          { required: true, message: 'ssh端口必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入ssh端口'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '服务器ip',
      key: 'server_ip',
      sortable: true,
      search: {
        component: {
          props: {
            clearable: true
          }
        }
      },
      type: 'input',
      form: {
        editDisabled: true,
        rules: [
          // 表单校验规则
          { required: true, message: '服务器ip必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入服务器ip'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '流媒体账号',
      key: 'lmt_username',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '流媒体账号必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入流媒体账号'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '流媒体密码',
      key: 'lmt_password',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '流媒体密码必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入流媒体密码'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '服务器账号',
      key: 'serve_username',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '服务器账号必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入服务器账号'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '服务器密码',
      key: 'server_password',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '服务器密码必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入服务器密码'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }, {
      title: '公钥',
      key: 'server_keygen',
      sortable: true,
      type: 'input',
      form: {
        rules: [
          { required: false, message: '进货时间必填' }
        ],
        component: {
          props: {
            clearable: true
          },
          placeholder: '请输入进货时间'
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    }
    ].concat(vm.commonEndColumns())
  };
};
