import os
import asyncio

from dotenv import load_dotenv
import websockets

from textual.app import App
from textual.widgets import RichLog


load_dotenv()

WS_URL = os.getenv("WS_URL")
WS_AUTH_TOKEN = os.getenv("WS_AUTH_TOKEN")


class BotApp(App):
    async def on_mount(self) -> None:
        self.ws_log = RichLog()
        await self.mount(self.ws_log)
        self.ws_log.write("CONNECTING...")
        asyncio.create_task(self.ws_loop())

    async def ws_loop(self):
        headers = {
            "Authorization": f"Bearer {WS_AUTH_TOKEN}"
        }

        try:
            async with websockets.connect(WS_URL, headers=headers) as ws:
                self.ws_log.write(f"CONNECTED: {WS_URL}")
                async for msg in ws:
                    self.ws_log.write(msg)
        except Exception as e:
            self.ws_log.write(f"WS ERROR: {e}")


if __name__ == "__main__":
    BotApp().run()
