import discord
import asyncio
from hanspell import spell_checker
from hanspell.constants import CheckResult
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='!')

with open('token.json', 'r') as f:
    tokens = json.load(f)

token = tokens['token']

@bot.event
async def on_ready():
    print(bot.user.name)
    game = discord.Game('맞춤법 검사')
    await bot.change_presence(status=discord.Status.online, activity=game)

grammar = True
errors = ""
except_word = ['ㅇㅇ']
servers = dict()
'''
@bot.event
async def on_guild_join(self, guild):
    servers[guild.id] = {'except':[], 'grammar':True}
'''
@bot.event
async def on_message(message):
    global except_csv
    global errors
    global grammar
    global except_word
    global servers
    print(servers)
    sent = message.content
    if sent == "!도움" or sent == "!도움말" or sent == "!help":
        embed = discord.Embed(title='Made by james1112#9248') # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다 
        embed.set_footer(text=f"{message.author.name}" ,icon_url = message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/690152774478069787/5386334eea41bbf178a099e7c1342237.png")
        embed.add_field(name='!맞춤법 <on/off>', value=f'맞춤법 기능을 키거나 끕니다.', inline=True)
        embed.add_field(name='!제외어 <단어>', value=f'맞춤법 검사에서 제외할 단어를 지정합니다.', inline=True)
        embed.add_field(name='알림', value=f'현재 DB를 구축하고 있어 특정명령어가 사용이 불가능 합니다.', inline=False)
        await message.channel.send(embed=embed)

    elif not message.author.bot and grammar == True and not sent in except_word:
        result = spell_checker.check(sent)
        result.as_dict()
        for key, value in result.words.items():
            print(key, value)
        if value == 1:
            errors = '맞춤법'
        elif value == 2:
            errors = '띄어쓰기'
        elif value == 3:
            errors = '표준어 의심'
        elif value == 4:
            errors = '통계적 의심'
        if value != 0:
            embed = discord.Embed(title='{}'.format(errors), description=f"`{sent}`(이)가 아니라 `{result.checked}`입니다. \n\n{message.author.mention}", color=0xFF4500) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다 
            embed.set_footer(text=f"{message.author.name} | made by james1112#9248",icon_url = message.author.avatar_url)
            # 하단에 들어가는 조그마한 설명을 잡아줍니다 
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다. 
            author = message.author
            print(author)
            '''
            role = discord.utils.get(message.guild.roles, name="Muted")
            await author.add_roles(role, reason="맞춤법을 지켜")
            ch = bot.get_channel(930689433047556207)
            morder = bot.get_user(923163922570301491)
            embed=discord.Embed(title=' ',color=0xFAA41B )
            embed.set_author(name=f'[MUTE] {message.author.name}',icon_url = message.author.avatar_url)
            embed.add_field(name='User', value=f'{message.author.mention}', inline=True)
            embed.add_field(name='Moderator', value=f'{morder.mention}', inline=True)
            embed.add_field(name='Reason', value='맞춤법을 지키세요', inline=True)
            await ch.send(embed=embed)
            await asyncio.sleep(4)
            await author.remove_roles(role)
            '''
    '''
    elif sent == "!맞춤법" or sent == "!맞춤법검사":
        embed = discord.Embed(title="!맞춤법", description=f"!맞춤법 <on/off>\n \n 맞춤법 기능을 키거나 끕니다.") # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다 
        embed.set_footer(text=f"{message.author.name}" ,icon_url = message.author.avatar_url)
        await message.channel.send(embed=embed
    elif sent == "!맞춤법 끄기" or sent == "!맞춤법 off" or sent == "!맞춤법검사 끄기" or sent == "!맞춤법검사 off":
        servers[message.channel.guild.id]['grammar'] = False
        await message.channel.send('맞춤법 검사가 꺼졌습니다. 다시 키시려면 `!맞춤법 on`를 입력하세요.')
    elif sent == "!맞춤법 켜기" or sent == "!맞춤법 on" or sent == "!맞춤법검사 켜기" or sent == "!맞춤법검사 on":
        servers[message.channel.guild.id]['grammar'] = True
        await message.channel.send('맞춤법 검사가 켜졌습니다. 끄시려면 `!맞춤법 off`를 입력하세요.')
    elif sent.startswith("!제외어") or sent.startswith("!금지어"):
        if sent[5::] == "":
            await message.channel.send(f'현재 맞춤법 제외어는 `{str(servers[message.channel.guild.id]["except"])}`가 있습니다.')
        else:
            servers[message.channel.guild.id]["except"].append(sent[5::])
            await message.channel.send(f"{sent[5::]}을(를) 맞춤법 제외어로 설정했습니다.")
    '''
bot.run(token)
