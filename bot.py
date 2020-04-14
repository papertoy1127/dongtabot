import discord
import asyncio
import time
import os
from math import *

def doesNothing(txt):
    return txt
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
    elif (message.content.split()[0]=="!각도계산")&(str(message.channel)=="각도_계산기"):
        if message.content=="!각도계산":
            await message.channel.send("!각도계산 <계산할 각도>")
        else:
            getAngle=str(message.content.split(maxsplit=1)[1])
            if "/" in getAngle:
                relativeAngle=int(eval(getAngle)*7)
            elif getAngle.isnumeric():
                relativeAngle=int(getAngle)*7
            else:
                await message.channel.send("```%s도는 현재 얼불춤에서 만들 수 없습니다.```" % (getAngle))
                return
            print(relativeAngle)
            if getAngle=="360":
                await message.channel.send("```스페이스 바를 눌러 360도를 만들 수 있습니다.```")
                return
            if getAngle=="0":
                await message.channel.send("```탭 키를 눌러 탭드스핀을 만들 수 있습니다.\n실제 미드스핀을 원하신다면, 연구에 참여해주세요!```")
                return
            angles=(0,30,45,60,90,120,135,150,180,210,225,240,270,300)
            check=0
            sendMsg="```\n"
            for i in angles:
                #print(i)
                for j in angles:
                    #print(j)
                    for k in range(5):
                        #print(k)
                        for m in range(7):
                            #print(m)
                            if relativeAngle==(((7*i+7*108*k+900*m)-7*j)%2520):
                                print(str((((7*i+7*108*k+900*m))-7*j)%2520)+":")
                                check+=1
                                if k==0:
                                    if m==0:
                                        sendMsg=sendMsg+("%d도와 %d도로 %d도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,j,relativeAngle/7))+"\n"
                                    else:
                                        sendMsg=sendMsg+("%f도(%d + (900/7 × %d)도)와 %d도로 %s도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,m,j,getAngle))+"\n"
                                else:
                                    if m==0:
                                        sendMsg=sendMsg+("%d도(%d + (108 × %d)도)와 %d도로 %d도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,k,j,relativeAngle/7))+"\n"
                                    else:
                                        sendMsg=sendMsg+("%f도(%d + (108 × %d) + (900/7 × %d)도)와 %d도로 %s도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,k,m,j,getAngle))+"\n"
                           
            if check==0:
                await message.channel.send("```%s도는 현재 얼불춤에서 만들 수 없습니다.```" % (getAngle))
            else:
                await message.channel.send(sendMsg+"```")
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
    elif (message.content.split()[0]=="!계산")&(str(message.channel)=="각도_계산기"):
        if message.content=="!계산":
            await message.channel.send("!계산 <수식>")
        else:
            try:
                result=str(eval(message.content.split()[1]))
                await message.channel.send("```결과: "+result+"```")
            except NameError:
                await message.channel.send("```잘못된 수식입니다.```")
            except ZeroDivisionError:
                await message.channel.send("```0으로 나눌 수 없습니다.```")

@client.event
async def on_member_join(member):
    ex = '안녕하세요 {0.mention}님, !역할지급 명령어로 역할_요청 채널에 역할을 요청해주세요!'
    channel = member.server.get_channel("가입")
    await client.send_message(channel, ex.format(member))

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
