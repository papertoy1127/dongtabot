import discord
import asyncio
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
    #await message.channel.send("test")
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
            await message.channel.send(message.content.split()[1]+" 역할을 찾을 수 없습니다. (일반인/연구원)")
    elif (message.content.split()[0]=="!광리자")&(str(message.channel)=="역할_요청"):
        role = discord.utils.get(message.guild.roles, name="광리자")
        await message.author.remove_roles(role)
    elif (message.content=="!MEE6 MEE6")&(str(message.channel)=="역할_요청"):
        await message.channel.send("뮥뮥")
    elif (message.content.split()[0]=="!me"):
        if (message.content=="!me")
            await message.channel.send(message.author.mention)
        else:
            await message.channel.send(message.content.split(maxsplit=1)[1])
    elif (message.content=="!you")&(str(message.channel)=="역할_요청"):
        await message.channel.send(client.user.mention)

@client.event
async def on_member_join(member):
    ex = '안녕하세요 {0.mention}님, !역할지급 명령어로 역할_요청 채널에 역할을 요청해주세요!'
    channel = member.server.get_channel("가입")
    await client.send_message(channel, ex.format(member))

#@client.event
#async def on_member_join(self):
#    ment = self.mention
#    await self.get_channel(697660178190958664).send("{has joined the server.")
access_token=os.environ["BOT_TOKEN"]
client.run("Njk3NzMxMjIwNTgyMTcwNjg2.Xo_VGg"+".2-weFLa6w14ChoLvgC3IFbbI9UY") #access_token)
