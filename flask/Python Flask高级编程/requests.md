#### request 安装
pipenv install requests

- get请求
```PYTHON
import requests

class HTTP:
    def get(self,url,return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            if return_json:
                return {}
            else:
                return ''
```

- 针对if--else优化：
```PYTHON
import requests

class HTTP:
    def get(self,url,return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else r.text
        return r.json() if return_json else r.text
```
