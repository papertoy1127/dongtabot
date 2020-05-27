import discord
import asyncio

class printMessage(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg

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
    if (message.content.split()[0]=="!각도계산")&(str(message.channel)=="각도계산"):
        text = message.content.split()[1]
        print(text)
        try:
            for i in text.split('/'):
                if i.isnumeric() == False:
                    raise printMessage('잘못된 각도입니다. D1')
            if len(text.split('/')) > 2:
                raise printMessage('잘못된 각도입니다. D2')
            if len(text.split('/')) == 2:
                if text.split('/')[1] != '7':
                    raise printMessage('잘못된 각도입니다. (분모를 7로 해주세요.)')
            if '/' in text:
                toGet = int(round(eval(text) * 7))
                heptaAngle = True
            else:
                toGet = int(text)
                heptaAngle = False
            angles=(0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300)
            check=[]
            sendMsg="```\n"
            for preAngle in angles:
                for latAngle in angles:
                    for penta in range(5):
                        if heptaAngle == False:
                            angle = (preAngle + penta * 108 - latAngle) % 360
                            if angle == toGet:
                                if penta == 0:
                                    check.append("{}° - {}° -> {}°".format(preAngle, latAngle, toGet))
                                else:
                                    check.append("{}° + 108 × {}° - {}° -> {}°".format(preAngle, penta, latAngle, toGet))
                        else:
                            for hepta in range(7): # 부동소수점 오차를 줄이기 위해 *7
                                angle = (preAngle * 7 + penta * 108 * 7 + hepta * 900 - latAngle * 7) % (360 * 7)
                                if angle == toGet:
                                    if penta == 0:
                                        check.append("{}° + 900/7 × {}° - {}° -> {}°".format(preAngle, hepta, latAngle, str(toGet) + '/7'))
                                    else:
                                        check.append("{}° + 108 × {}° + 900/7 × {}° - {}° -> {}°".format(preAngle, penta, hepta, latAngle, str(toGet) + '/7'))
            if check:
                raise printMessage(check)
            else:
                if heptaAngle == False:
                    raise printMessage(str(toGet) + '도는 현재 만들 수 없습니다.')
                else:
                    raise printMessage(str(toGet) + '/7도는 현재 만들 수 없습니다.')
        except printMessage as m:
            if type(m.msg) == list:
                msg = '```\n'
                for i in m.msg:
                    msg += i + '\n'
                msg += '```'
                await message.channel.send(msg)
            else:
                await message.channel.send('```' + str(m.msg) + '```')

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
