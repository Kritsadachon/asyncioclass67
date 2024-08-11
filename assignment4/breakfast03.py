import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare")
    sleep(1)
    print("coffee waiting...")
    await asyncio.sleep(5)  # pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():
    print("eggs: prepare ingredients")
    sleep(1)
    print("egg frying...")
    await asyncio.sleep(3)  # pause, another tasks can be run
    print("eggs: ready")

async def main():
    start = time()
    await asyncio.gather(make_coffee(),fry_eggs()) #6.01
    # coffee = asyncio.create_task(make_coffee())
    # egg = asyncio.create_task(fry_eggs())
    # await coffee
    # await egg #แบบนี้ได้ 6.0sec
    # await asyncio.gather(coffee,egg) #6.01
    print(f"breakfast is ready in {time()-start:.2f} sec")

asyncio.run(main())
