from quart import Quart, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon

app = Quart(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()
    return pokemon

async def get_pokemons():
    rand_list = [random.randint(1, 151) for _ in range(5)]
    pokemon_data = []

    async with httpx.AsyncClient() as client:
        tasks = []
        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        pokemons_json = await asyncio.gather(*tasks)
        for pokemon_json in pokemons_json:
            pokemon_object = Pokemon(pokemon_json)
            pokemon_data.append(pokemon_object)

    return pokemon_data

@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons() 
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return await render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50002)
