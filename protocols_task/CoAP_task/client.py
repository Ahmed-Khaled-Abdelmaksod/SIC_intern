import asyncio
from aiocoap import Context, Message, GET
import time
async def main():
    client = await Context.create_client_context()
    i = 0
    while i < 60:
        request = Message(code=GET, uri="coap://localhost/temperature")

        response = await client.request(request).response
        print(response.payload.decode())
        i += 1
        time.sleep(1)
if __name__ == "__main__":
    asyncio.run(main())