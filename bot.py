import discord
from discord.ext import commands, tasks
from random import randrange

bot = commands.Bot(command_prefix='!')

#rooms = ["SE", "E1", "E2", "E3", "E4", "NE", "NE1", "NE2", "MIDDLE", "SE1", "SE2", "SE_LAST", "END", "ERROR", "N1", "N2", "N3", "N4", "NW", "NW1", "NW2", "MIDDLE", "ERROR", "W1", "W2", "W3", "W4", "SW", "S1", "S2", "S3", "S4", "SE_LAST", "ERROR", "SW1", "SW2", "SW"]
rooms = ["SE", "E1", "E2", "E3", "E4", "NE", "N1", "N2", "N3", "N4", "NW", "W1", "W2", "W3", "W4", "SW", "S1", "S2", "S3", "S4", "SE_LAST", "SE_LAST", "SE_LAST", "SE_LAST", "SE_LAST", "NE1", "NE2", "MIDDLE", "SW1", "SW2", "SW", "S1", "S2", "S3", "S4", "NW1", "NW2", "MIDDLE", "SE1", "SE2", "SE_LAST", "SE_LAST", "SE_LAST", "SE_LAST", "SE_LAST"]

answers = {
    "SE": "START", 
    "E1": "추석", 
    "E2": "26", 
    "E3": "7", 
    "E4": "효모", 
    "NE": "759405941057388594", 
    "NE1": "☢️", 
    "NE2": "🍗", 
    "MIDDLE": "😈", 
    "SE1": "🇹🇷", 
    "SE2": "105", 
    "SE_LAST": "더도 말고 덜도 말고 한가위만 같아라", 
    "N1": "v", 
    "N2": "105", 
    "N3": "🍁", 
    "N4": "한가위", 
    "NW": "당신의 노고에 언제나 감사를", 
    "NW1": "↘️", 
    "NW2": "paperpptxyzwrdawngmdmc01", 
    "W1": "10월 4일", 
    "W2": "2018년 1월 31일", 
    "W3": "yellow", 
    "W4": "cage", 
    "SW": "거품", 
    "S1": "Rammasun", 
    "S2": ":", 
    "S3": "WIP", 
    "S4": "♌", 
    "SW1": "🤔", 
    "SW2": "super"}
DG = {
    1: '**도**가',
    2: '**개**가',
    3: '**걸**이',
    4: '**윷**이',
    5: '**모**가'
}

players = dict()

def appender(ref, ap):
    ref[0].append(ap)

def dictor(ref, key, value):
    ref[0][key] = value

def clear(ref):
    ref[0] = dict()
    return "초기화 되었습니다."

@bot.event
async def on_ready():
    print("---연결 성공---")
    print("봇 이름: {bot.user.name}")
    print("ID: {bot.user.id}")

@bot.command()
async def edit(ctx, arg):
    await ctx.send(arg + " >> " + str(eval(arg)))

@bot.command()
async def check(ctx, *args):
    global players
    Server = bot.get_guild(759384886174810122)
    if isinstance(ctx.channel, discord.channel.DMChannel):
        try:
            if players[ctx.author]:
                pass
        except KeyError:
            players[ctx.author] = []
        ctx.send(players[ctx.author])
        try:
            qus = str(args[0]).upper()
            ans =  (' '.join(args[1:len(args)])).upper()
        except IndexError:
            embed = discord.Embed(title = "", description="명령어가 완전하지 않습니다\n(올바른 사용법: `!check <문제> <답>`)", color=0x999999)
            await ctx.send("", embed = embed)
            return
        try:
            #await ctx.send("```"+answers[qus].upper()+ans+"```")
            if qus in players[ctx.author]:
                embed = discord.Embed(title = "", description="이미 푼 문제입니다.", color=0x999999)
                await ctx.send("", embed = embed)
                return
            if answers[qus].upper() == ans:
                await ctx.send("정답!")
                appender([players[ctx.author]], qus)
                author = Server.get_member(ctx.author.id)
                tmp = randrange(1,6)
                roleName = rooms[(rooms.index(qus)+tmp)]
                role = discord.utils.get(Server.roles, name=roleName)
                await author.add_roles(role)
                embed = discord.Embed(title = "", description="%s 나와 %s 칸으로 이동했습니다." % (DG[tmp], role), color=0x999999)
                await ctx.send("", embed = embed)
 
            else:
                await ctx.send("오답!")
        except KeyError as E:
            embed = discord.Embed(title = "", description="%s는 없는 문제입니다" % E, color=0x999999)
            await ctx.send("", embed = embed)
    else:
        embed = discord.Embed(title = "", description="이 명령어는 DM으로만 사용할 수 있습니다", color=0x999999)
        await ctx.send("", embed = embed)

token = "NzMxMDUyNzIzMjQzNDUwMzY5.Xwgb5w."+"bUurs0v4GiziGZw5preirNeEIEI"

bot.run(token)
