# Import the asyncio library to handle asynchronous operations
import asyncio

# Define a coroutine function that accepts a value as input
async def task(value):
    # Simulate some waiting time by pausing the task for 1 second
    await asyncio.sleep(1)
    # Return a value that is 100 times the input value
    return value * 100

# Define the main coroutine function where multiple tasks are created
async def main():
    # Create a task group to manage and run multiple asynchronous tasks
    async with asyncio.TaskGroup() as group:
        # Create and issue tasks for values in the range of 1 to 10
        # The tasks are stored in a list and each task is created with 'group.create_task(task(i))'
        tasks = [group.create_task(task(i)) for i in range(1, 10)]
    
    # After the task group completes, loop through each task
    # Print the result (output) of each task using the .result() method
    for t in tasks:
        print(t.result())

# Entry point to start the asyncio event loop and run the 'main' coroutine
asyncio.run(main())