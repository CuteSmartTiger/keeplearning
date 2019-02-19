{% for minion_id in data['present'] %}
present_for_{{ loop.index }}:
  local.cmd.run:
    - tgt: {{ minion_id }}
    - arg:
      - echo {{ minion_id }} 
{% endfor %}


{# show_full_context() #}

