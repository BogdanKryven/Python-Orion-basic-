import asyncio


@asyncio.coroutine
def print_nums():
    num = 0
    while True:
        num += 1
        print(num)
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_msg():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds passed")
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_msg())
    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()
