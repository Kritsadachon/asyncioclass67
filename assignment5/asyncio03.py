# example of waiting for the first task to fail
from random import random
import asyncio

async def task_coro(arg):
    # generate a random value 0-1
    value = random()
    # block
    await asyncio.sleep(value)
    #report value
    print(f'> task {arg} done with {value}')
    # conditionally fail
    if value < 0.5: 
        raise Exception(f' Something bad happend in {arg}')
    
async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait first complete
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    #report result
    print('DONE')
    first = done.pop()
    print(first)

asyncio.run(main())