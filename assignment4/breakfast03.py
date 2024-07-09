# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee(): #1
    print("coffee: prepare")
    sleep(1)
    print("coffee waiting")
    await asyncio.sleep(5)