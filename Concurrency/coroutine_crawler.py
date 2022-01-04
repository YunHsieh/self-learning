import asyncio
import time
import requests

now = lambda: time.time()
loop = asyncio.get_event_loop()


def task1(val):
    print(f'inpurt data: {val}')
    r = requests.get(**val)
    print(f'response {r}')
    return r

async def dosomething(url):
    print(f"entry coroutine run url: {url}")
    parms = {
        'url': url,
        'headers': {
            'Cookie': 'ckFORUM_bsn=60076'
        }
    }
    res = await loop.run_in_executor(None, task1, parms)
    print(f"finished")

if __name__ == "__main__":
    urls = [
        'https://forum.gamer.com.tw/A.php?bsn=60076',
        'https://forum.gamer.com.tw/A.php?bsn=30861',
    ]
    start = time.time()
    tasks = [asyncio.ensure_future(dosomething(i)) for i in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    print('total time: ', now() - start)
