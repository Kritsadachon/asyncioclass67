# example of waiting for the first task to complete
from random import random
import asyncio

# corountine to execute in a new task
async def task_coro(arg):
    # generate a random value 0-1
    value = random()
    # block
    await asyncio.sleep(value)
    # report value
    print(f'task > {arg} done with {value}')

async def main():
    #create many task
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #report result
    print('done')
    # get the first task to complete
    first = done.pop()
    print(first)

asyncio.run(main())