#### json
```PYTHON
# 优化前
return json.dumps(result),200,{'content-type':'application/json'}


# 优化后
return jsonify(result)
```
