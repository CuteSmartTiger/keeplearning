{% if data['fun'] == 'saltutil.sync_grains' and data['retcode'] == 0 %}
send_event_cust_grains_sync_done:
  local.event.send:
    - tgt: {{ data['id'] }}
    - arg:
      - cust/grains_sync_done
{% endif %}
