# example of creating an event loop
import asyncio
async def some_async_task():
    print("sleep for 1 sec")
    await asyncio.sleep(1)
    print("done")

# Get the current event loop
loop = asyncio.get_event_loop()

# Run loop untill coroutine is completed
loop.run_until_complete(some_async_task())