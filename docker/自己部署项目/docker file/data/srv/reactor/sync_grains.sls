mission1:
  local.saltutil.sync_grains:
    - tgt: {{ data['id'] }}
