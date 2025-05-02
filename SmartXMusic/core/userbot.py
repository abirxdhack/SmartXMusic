from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.client = Client(
            name="SmartXAss",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING_SESSION),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant User Client...")
        await self.client.start()
        try:
            await self.client.join_chat("TheSmartDev")
            await self.client.join_chat("abirxdhackz")
        except:
            pass
        assistants.append(1)
        try:
            await self.client.send_message(config.LOGGER_ID, "Bro Assistant Started Successfully!")
        except:
            LOGGER(__name__).error(
                "You Must Make Assitant Account Admin Of Your Logs Channel/Group"
            )
            exit()
        self.client.id = self.client.me.id
        self.client.name = self.client.me.mention
        self.client.username = self.client.me.username
        assistantids.append(self.client.id)
        LOGGER(__name__).info(f"Assistant Successfully Started as {self.client.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistant User Client !...")
        try:
            await self.client.stop()
        except:
            pass
