#print("hello world")
import asyncio
import time

async def waiter(n):
    await asyncio.sleep(n)
    print(f"waited for {n} sec")

async def main(): 
    print(time.strftime('%X'))
    await waiter(2)
    await waiter(3)
    print(time.strftime('%X'))
   # print("hello ")
    #await asyncio.sleep(1)
    #print("world")

if __name__ == '__main__':
    asyncio.run(main())
