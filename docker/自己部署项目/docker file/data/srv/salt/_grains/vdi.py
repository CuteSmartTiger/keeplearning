import salt.utils

# Solve the Chicken and egg problem where grains need to run before any
# of the modules are loaded and are generally available for any usage.
import salt.modules.cmdmod

__salt__ = {
    'cmd.run': salt.modules.cmdmod._run_quiet,
    'cmd.retcode': salt.modules.cmdmod._retcode_quiet,
    'cmd.run_all': salt.modules.cmdmod._run_all_quiet
}

def uuid():
    _grains = {}
    if salt.utils.is_windows():
	_grains['uuid'] = __salt__['cmd.run']('cscript //nologo C:\\salt\\getuuid.vbs')
    else:
	_grains['uuid'] = __salt__['cmd.run']('xenstore-read vm | xargs -n1 basename || echo None')


    return _grains

def vdi_version():
    _grains = {}
    if salt.utils.is_windows():
	_grains['vdi_agent_version'] = __salt__['cmd.run']('C:\\Program Files\\VDIAgent\\checkversion.exe c')
	_grains['vdi_terminal_version'] = ''
    else:
	_grains['vdi_agent_version'] = ''
	_grains['vdi_terminal_version'] = __salt__['cmd.run']('python /opt/thinclient/tc_upgrade.py --version')

    return _grains




