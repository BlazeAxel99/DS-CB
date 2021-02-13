import asyncio
import aiohttp

async def fetchFromGoogle():
    url = 'https://www.google.com'
    session = aiohttp.ClientSession()
    resp =  await session.get(url)
    print(resp)
    await session.close()

async def main():
    await fetchFromGoogle()
    
if __name__ == '__main__':
    asyncio.run(main()) 
    #rest code in jp notebook