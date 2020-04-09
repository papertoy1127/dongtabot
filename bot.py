import discord
import os

client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.content.split()[0]=="!역할지급")&(str(message.channel)=="역할_요청"):
        if message.content=="!역할지급":
            await message.channel.send("!역할지급 [일반인|연구원]")
        elif message.content.split()[1]=="일반인":
            role = discord.utils.get(message.guild.roles, name="연구원")
            await message.author.remove_roles(role)
            role = discord.utils.get(message.guild.roles, name="승인됨")
            await message.author.add_roles(role)
            role = discord.utils.get(message.guild.roles, name="일반인")
            await message.author.add_roles(role)
            await message.channel.send("일반인 역할이 지급되었습니다.")
        elif message.content.split()[1]=="연구원":
            role = discord.utils.get(message.guild.roles, name="일반인")
            await message.author.remove_roles(role)
            role = discord.utils.get(message.guild.roles, name="승인됨")
            await message.author.add_roles(role)
            role = discord.utils.get(message.guild.roles, name="연구원")
            await message.author.add_roles(role)
            await message.channel.send("연구원 역할이 지급되었습니다.")
        elif message.content.split()[1]=="관리자":
            role = discord.utils.get(message.guild.roles, name="광리자")
            await message.author.add_roles(role)
            await message.channel.send("_광_리자 역할이 지급되었습니다.")
        elif message.content.split()[1]=="광리자":
            role = discord.utils.get(message.guild.roles, name="광리자")
            await message.author.add_roles(role)
            await message.channel.send("광리자 역할이 지급되었습니다.")
        elif message.content.split()[1]=="모나리자":
            role = discord.utils.get(message.guild.roles, name="모나리자")
            await message.author.add_roles(role)
            await message.channel.send("모나리자 역할이 지급되었습니다.")
        elif message.content.split()[1]=="0도미드스핀의발견자":
            await message.channel.send("핫덕님 겁니다.")
        else:
            await message.channel.send(message.content.split()[0]+" 역할을 찾을 수 없습니다. (일반인/연구원)")
    elif (message.content.split()[0]=="!광리자")&(str(message.channel)=="역할_요청"):
        role = discord.utils.get(message.guild.roles, name="광리자")
        await message.author.remove_roles(role)

#@client.event
#async def on_member_join(self):
#    ment = self.mention
#    await self.get_channel(697660178190958664).send("{has joined the server.")
access_token=os.environ["BOT_TOKEN"]
client.run("jKKyDbVUvwvV7v4nZbZscyivJDELVwEg")
