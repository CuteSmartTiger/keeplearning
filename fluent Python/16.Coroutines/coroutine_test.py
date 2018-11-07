import time


def get_html():
    time.sleep(2)
    pass


def parse_url():
    time.sleep(2)
    pass


def get_url(url):
    # 此处耗时
    html = get_html(url)  # 此处暂停切换到另一个函数去执行
    urls = parse_url(url)


def get_url1(url):
    # 此处耗时
    html = get_html(url)  # 此处暂停切换到另一个函数去执行
    urls = parse_url(url)

# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复函数的继续执行
# 因此出现协程，一个有多个入口的函数，可以暂停的函数（暂停的地方可以传入值）
