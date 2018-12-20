import asyncio

import aiohttp


async def test_single_proxy(proxy):

    async with aiohttp.ClientSession() as session:

        real_proxy = 'http://' + proxy
        print('Testing', proxy)
        async with session.get("http://www.baidu.com", proxy=real_proxy, timeout=30) as response:
            if response.status == 200:
                print('代理ip成功：', proxy)



loop = asyncio.get_event_loop()
list = ["47.94.230.42:9999", "59.57.151.126:31689", "59.37.33.62:50686"]
tasks = [test_single_proxy(proxy) for proxy in list]
loop.run_until_complete(asyncio.wait(tasks))


