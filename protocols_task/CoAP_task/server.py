from aiocoap import resource,Context,Message
import asyncio
import random
class TempResourse(resource.Resource):
    
    async def render_get(self,request):
        temp = random.randint(25,27)
        payload = f"Temp : {temp} "
        print(payload)
        return Message(payload=payload.encode("utf-8"))
async def main():
    root = resource.Site()
    root.add_resource(["temperature"],TempResourse())
    print("Server Started: hello Sir Abdelmaksod :)")
    await Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()
    

if __name__ == '__main__':
    asyncio.run(main())
    

