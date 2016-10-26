import asyncio
async def hello():
    print('hello,world')
    r=await asyncio.sleep(1)
    print('hello,again')
    
