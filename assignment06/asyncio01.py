import asyncio

class AsyncDatabaseConnection :
    def __init__(self, db_name):
        self.db_name = db_name

    async def __aenter__(self):
        print(f"Connecting to DB {self.db_name}...")
        await asyncio.sleep(1) # Sim async connect setup
        print(f"Connected to the DB {self.db_name}.")
        return self
    
    async def __aexit__ (self, exc_type, exc, tb):
        print(f"Closing the db connection to {self.db_name}...")
        await asyncio.sleep(1) #sim async connection teardown
        print(f"CLose the db connection to {self.db_name}.")
        if exc:
            print(f"An exception occurred: {exc}")

    async def fetch_data(self):
        await asyncio.sleep(1) # Sim an sync data fetch
        return {"data" : "sample data"}
    
async def main():
    async with AsyncDatabaseConnection("test_db") as db:
        data = await db.fetch_data()
        print(f"Fetched data: {data}")

#Running the async main func
asyncio.run(main())