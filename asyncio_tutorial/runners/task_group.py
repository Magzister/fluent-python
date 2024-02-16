import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "Hello"))
        tg.create_task(say_after(2, "world"))
        print(f"started at {time.strftime("%X")}")

    print(f"finished at {time.strftime("%X")}")

asyncio.run(main())
