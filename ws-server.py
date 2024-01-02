import asyncio
import websockets

connected = set()

async def chat(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            # Loop through all connected clients
            for conn in connected:
                if conn == websocket:
                    # If the current connection is the sender
                    await conn.send(f"You said: {message}")
                else:
                    # If the current connection is not the sender
                    await conn.send(f"Someone said: {message}")
    finally:
        connected.remove(websocket)

start_server = websockets.serve(chat, "0.0.0.0", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
