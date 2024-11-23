import asyncio

async def task1():
    print("Starting Task 1")
    await asyncio.sleep(2)  # Non-blocking wait
    print("Task 1 Completed")

async def task2():
    print("Starting Task 2")
    await asyncio.sleep(3)  # Non-blocking wait
    print("Task 2 Completed")

async def main():
    await asyncio.gather(task1(), task2())  # Run tasks concurrently

asyncio.run(main())
