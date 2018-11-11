# 与asyncio同步与通信结合看
# 使用asyncio时，单线程无需加锁
import asyncio

total = 0


async def add(ran):
    """
    :param ran: int
    :return: int
    """
    global total
    for i in range(ran):
        total += 1
    print(total)
    return total


async def sub(ran):
    """
    :param ran: int
    :return: int
    """
    global total
    for i in range(ran):
        total -= 1
    print(total)
    return total


# 在main一个主线程下开辟了两个子线程
if __name__ == "__main__":
    import asyncio

    tasks = [add(100000), sub(100000)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)
