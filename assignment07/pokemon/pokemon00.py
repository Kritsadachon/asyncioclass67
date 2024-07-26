import aiofiles
import asyncio
import json

pokemonapi_directory = '/Users/kritsadachonchansawang/Documents/GitHub/asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = '/Users/kritsadachonchansawang/Documents/GitHub/asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())