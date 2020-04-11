import discord
import asyncio
import time
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
            await message.channel.send("!역할지급 <일반인|연구원>")
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
        await message.channel.send(str(message.author.mention))
    elif (message.content.split()[0]=="!you"):
        role = discord.utils.get(message.guild.roles, name="연구소장")
        if role in message.author.roles:
            await message.delete()
            await message.channel.send(message.content.split(maxsplit=1)[1])
        else:
            await message.channel.send("관리자만 사용할 수 있는 명령어 입니다.")
    elif (message.content.split()[0]=="!do"):
        role = discord.utils.get(message.guild.roles, name="연구소장")
        if role in message.author.roles:
            eval(message.content.split(maxsplit=1)[1])
        else:
            await message.channel.send("관리자만 사용할 수 있는 명령어 입니다.")
    elif (message.content.split()[0]=="!doa"):
        role = discord.utils.get(message.guild.roles, name="연구소장")
        if role in message.author.roles:
            await eval(message.content.split(maxsplit=1)[1])
        else:
            await message.channel.send("관리자만 사용할 수 있는 명령어 입니다.")
    elif (message.content.split()[0]=="!dodel"):
        role = discord.utils.get(message.guild.roles, name="연구소장")
        if role in message.author.roles:
            await message.delete()
            eval(message.content.split(maxsplit=1)[1])
        else:
            await message.channel.send("관리자만 사용할 수 있는 명령어 입니다.")
    elif (message.content.split()[0]=="!doadel"):
        role = discord.utils.get(message.guild.roles, name="연구소장")
        if role in message.author.roles:
            await message.delete()
            await eval(message.content.split(maxsplit=1)[1])
        else:
            await message.channel.send("관리자만 사용할 수 있는 명령어 입니다.")

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
