import asyncio
from random import random

# coroutine to simulate cooking food
async def cook_food(arg):
    cook = 1 + random()
    print(f'Microwave ({arg}): Cooking {cook:.7f} seconds...')
    await asyncio.sleep(cook)
    print(f'Microwave ({arg}): Finished cooking')
    return arg, cook

# main coroutine
async def main():
    # create tasks for cooking different foods
    tasks = [
        asyncio.create_task(cook_food("Rice")),
        asyncio.create_task(cook_food("Noodle")),
        asyncio.create_task(cook_food("Curry")),
    ]

    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # get the first completed task result
    for task in done:
        first_completed, time_taken = task.result()
        gg = task.result()
        print(gg)
        print(f'Completed task: 1\n - {first_completed} is completed in {time_taken:.7f}')

    # print details of pending tasks
    print(f'Uncompleted task: {len(pending)}')
# start the asyncio program
asyncio.run(main())