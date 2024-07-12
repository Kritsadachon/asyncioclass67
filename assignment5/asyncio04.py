# example of waiting for all tasks to be completed with a timeout
from random import random
import asyncio

async def task_coro(arg):
    value = random() * 10
    # block 
    await asyncio.sleep(value)
    #report value
    print(f'> task {arg} done with {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all task to complete
    done, pending = await asyncio.wait(tasks, timeout=5)
    print(f'Done, {len(done)} tasks complete in time')

asyncio.run(main())