# example of running a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coro
    await asyncio.sleep(1)

# main 
async def main():
    # exec my custom coroutine
    await custom_coro()

asyncio.run(main())