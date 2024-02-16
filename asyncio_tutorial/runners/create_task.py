import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task = asyncio.create_task(say_after(2, "world"))
    print("Hello")
    await task


asyncio.run(main())
