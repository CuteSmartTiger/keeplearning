```

#!/bin/bash
sudo mv /var/lib/dpkg/info  /var/lib/dpkg/info_old
sudo mkdir /var/lib/dpkg/info
sudo apt-get update
sudo apt-get -f install
sudo mv /var/lib/dpkg/info/*   /var/lib/dpkg/info_old
sudo rm -rf  /var/lib/dpkg/info
sudo mv  /var/lib/dpkg/info_old  /var/lib/dpkg/info

sudo apt-get install python-gevent
```



https://pypi.org/project/greenlet/#files

下载包：https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
