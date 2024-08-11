# example of gather for many coroutines in a list
import asyncio 

# coroutine used for a task
async def task_coro(value):
    # report a msg
    print(f' >task {value} execting')
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point
async def main():
    # report msg
    print('main starting')
    coros = [task_coro(i) for i in range(10)]
    await asyncio.gather(*coros)
    print('main done')

asyncio.run(main())