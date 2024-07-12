# example of waiting for all tasks to complete
from random import random
import asyncio

async def task_coro(arg):
    # generate value 0-1
    value = random()
    # block for moment
    await asyncio.sleep(value)
    # repoty value
    print(f'>task {arg} done with {value}')

async def main():
    # create many task 
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all task to complete
    done, pending = await asyncio.wait(tasks)
    #report result
    print('All done')

asyncio.run(main())