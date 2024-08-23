# Import the asyncio library, which provides support for asynchronous programming.
import asyncio

# Define the first coroutine function, task1.
async def task1():
    # Print a message indicating the start of task 1.
    print('Hello from coroutine 1')
    # Pause execution for 1 second to simulate waiting.
    await asyncio.sleep(1)

# Define the second coroutine function, task2.
async def task2():
    # Print a message indicating the start of task 2.
    print('Hello from coroutine 2')
    # Pause execution for 1 second to simulate waiting.
    await asyncio.sleep(1)

# Define the third coroutine function, task3.
async def task3():
    # Print a message indicating the start of task 3.
    print('Hello from coroutine 3')
    # Pause execution for 1 second to simulate waiting.
    await asyncio.sleep(1)

# Define the main function to manage task execution.
async def main():
    # Create a task group to manage multiple asynchronous tasks.
    async with asyncio.TaskGroup() as group:
        # Create and schedule task1.
        group.create_task(task1())
        # Create and schedule task2.
        group.create_task(task2())
        # Create and schedule task3.
        group.create_task(task3())
    # Print a message when all tasks have completed.
    print('Done')

# Run the asyncio event loop and execute the main function.
asyncio.run(main())