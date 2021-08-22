import asyncio


async def print_nums():
    num = 0
    while True:
        num += 1
        print(num)
        await asyncio.sleep(1)


async def print_msg():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds passed")
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_msg())
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()