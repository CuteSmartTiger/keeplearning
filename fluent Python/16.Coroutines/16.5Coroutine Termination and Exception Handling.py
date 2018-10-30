class DemoException(Exception):
    """为这次演示定义的异常类型。"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        # 若为其他异常，则无法处理
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


# 显式地把异常发给协程。
# generator.throw(exc_type[, exc_value[, traceback]])
# enerator.close()


exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
print(exc_coro.throw(DemoException))
exc_coro.close()
from inspect import getgeneratorstate

print(getgeneratorstate(exc_coro))

print('-----------------------分割线------------------------')

# 思考：try与finally是如何解决清理的
# 如果不管协程如何结束都想做些清理工作，要把协程定义体中相关的代
# 码放入 try/finally 块中

class DemoException(Exception):
    """为这次演示定义的异常类型。"""


def demo_exc_handling():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            # 若为其他异常，则无法处理
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
print(exc_coro.throw(DemoException))
exc_coro.close()
from inspect import getgeneratorstate

print(getgeneratorstate(exc_coro))