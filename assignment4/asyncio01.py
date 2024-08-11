# example of getting the current task from the main coroutine
import asyncio

async def main():
    # report a msg
    print('main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report task details
    print(task)

asyncio.run(main())