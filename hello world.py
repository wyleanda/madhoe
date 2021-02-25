import discord
import asyncio
import random


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member): # welcome message shit
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
        await member.send('Hi! Welcome to our server, in 2 minutes you will get "Verified" role, please read rules in that time.')
        await asyncio.sleep(120)   #The parameter is in seconds, so it'll wait for 120 seconds
        verifiedRole = discord.utils.get(member.guild.roles, id = 810719173889884160)
        await member.add_roles(verifiedRole)

    
    async def on_message(self, message): # guessing game shit
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))




intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

client.run('ODE0MjE1NjYzODk1ODM4NzMx.YDanbQ.QLwbmkj7nKN1wEUIG__56__bk04')