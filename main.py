import discord
import asyncio
from datetime import datetime
import pandas as pd

check = '\N{SKULL}'
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        general = pd.DataFrame(columns=['Author', 'Content'])
        server = client.get_guild(741561732761387048)
        target = client.get_user(807945971576602665)
        channel = client.get_channel(775550200928272385)
        check = await server.fetch_emoji(987396989144678490)
        async for message in channel.history(limit=10000000000):
            x = [message.author, message.content, message.created_at]
            message_series = pd.DataFrame([x], columns=['Author', 'Content', 'temp'])
            message_series = message_series.set_index('temp')
            general = pd.concat([general, message_series], ignore_index=False)
            print(general)
            general.to_csv('general_channel.csv')
            if message.author == target:
                await message.add_reaction(check)
                await asyncio.sleep(0.3)
            else:
                await asyncio.sleep(0.0005)

    #async def on_message(self, message):
        #target = client.get_user(0)
        #server = client.get_guild(0)
        #check = await server.fetch_emoji(0)
        #if message.author != target:
        #    return
        
        #else:
            #await message.add_reaction(check)            

client = MyClient()
client.run('ODM5NDA0MTA1MDM3OTA1OTMw.GvmYS6.2m8rrD9f5In5u7JhoB1MpoOtSs7Wh3T4OjDrSU')