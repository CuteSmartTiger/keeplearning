mission1:
  local.saltutil.sync_grains:
    - tgt: {{ data['id'] }}
#highstate_and_cmd:
#  local.state.highstate:
#    - tgt: {{ data['id'] }}
#  local.cmd.run:
#    - tgt: {{ data['id'] }}
#    - arg:
#      - rm -rf /tmp/*
