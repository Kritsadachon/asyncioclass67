from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time

async def get_ability_id(client, ability_name):
    url = f'https://pokeapi.co/api/v2/ability/{ability_name}/'
    resp = await client.get(url)
    ability = resp.json()
    return ability['id']

async def get_pokemon_with_ability(client, ability_id):
    url = f'https://pokeapi.co/api/v2/ability/{ability_id}/'
    resp = await client.get(url)
    ability_data = resp.json()
    
    pokemon_urls = [pokemon['pokemon']['url'] for pokemon in ability_data['pokemon']]
    tasks = [asyncio.create_task(client.get(url)) for url in pokemon_urls]
    responses = await asyncio.gather(*tasks)
    
    pokemons = [Pokemon(resp.json()) for resp in responses]
    return pokemons

async def index():
    start_time = time.perf_counter()

    async with httpx.AsyncClient() as client:
        abilities = ['battle-armor', 'speed-boost']
        ability_ids = await asyncio.gather(*[get_ability_id(client, ability) for ability in abilities])
        tasks = [get_pokemon_with_ability(client, ability_id) for ability_id in ability_ids]
        results = await asyncio.gather(*tasks)
        
        ability_pokemons = {ability: pokemons for ability, pokemons in zip(abilities, results)}
        
        end_time = time.perf_counter()
        print(f"{time.ctime()} - Found Pokémon with abilities {', '.join(abilities)}. Time taken: {end_time-start_time:.2f} seconds")
        
        for ability, pokemons in ability_pokemons.items():
            print(f"\nPokémon with {ability}:")
            print(f"Total number of {ability}: {len(pokemons)}")
            for pokemon in pokemons:
                print(f"- {pokemon.name}")

if __name__ == '__main__':
    asyncio.run(index())
