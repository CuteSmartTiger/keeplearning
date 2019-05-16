etcd设置过期时间
lock = client.get_lock('/customer1', ttl=60)
