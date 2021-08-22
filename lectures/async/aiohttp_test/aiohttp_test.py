import asyncio
import aiohttp
import time


def write_file(data):
    file_name = f"{int(time.time() * 1000)}"
    with open(f"aiohttp_test/{file_name}.jpg", "wb") as file:
        file.write(data)


async def get_content(url, session, i):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        print(i)
        # write_file(data)


async def main():
    url = "https://loremflickr.com/320/240"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(20):
            task = asyncio.create_task(get_content(url, session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time.time()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    print(time.time() - t0)
