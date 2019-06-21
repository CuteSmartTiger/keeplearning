# apps status code
SUCCESS_STATUS = 0
FAIL_STATUS = 1

# need_paginate
NEED_PAGINATE = 'Y'
NOT_NEED_PAGINATE = 'N'

# Todo or history
RELATION = '0'
HISTORY = '1'

# role
DEV = 'DEV'
OPS = 'OPS'
QA = 'QA'
APPROVER = 'APPROVER'
ADMIN = 'ADMIN'
DBA = 'DBA'
PM = 'PM'

# tenant name
BKJK = '贝壳金控'

# bkjk workflow action
ACTION_APPROVE = 'approve'
ACTION_CANCEL = 'cancel'
ACTION_REJECT = 'reject'

# bkjk workflow status
WAIT_QA = 1
WAIT_APPROVE = 2
WAIT_OPS = 3
WAIT_DEV = 4
DONE = 5
CANCEL = 6
REJECT = 7

# base url
BASE_DEPLOY_URL = 'https://dalmore.bkjk-inc.com/#/deploy/detail/{deploy_id}'
BASE_CHANGE_URL = 'https://dalmore.bkjk-inc.com/#/change/detail/{change_id}'
