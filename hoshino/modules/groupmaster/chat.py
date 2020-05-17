import random
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
async def say_sorry(session):
    await session.send('ごめんなさい！嘤嘤嘤(〒︿〒)')

@sv.on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=True)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
    else:
        await session.send('mua~')

@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('你给我滚！', at_sender=True)
    
@sv.on_command('我喜欢你', aliases=('我爱你', '亲亲'), only_to_me=True)
async def chat_laogong(session):
    await session.send('诶嘿嘿，mua~', at_sender=True)

@sv.on_command('mua', only_to_me=True)
async def chat_mua(session):
    await session.send('笨蛋~', at_sender=True)

@sv.on_command('来点星奏', only_to_me=False)
async def seina(session):
    await session.send(R.img('星奏.png').cqcode)

@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=False)
async def ddhaole(session):
    await session.send('那个朋友是不是你弟弟？')
    await util.silence(session.ctx, 30)

@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    await util.silence(session.ctx, 30)

@sv.on_command('所有的努力全部木大', only_to_me=False)
async def nihaole(session):
    await session.send('不要停下来啊！\nₘₙⁿ\n▏n\n█▏　､⺍\n█▏ ⺰ʷʷｨ\n█◣▄██◣\n◥██████▋\n　◥████ █▎\n　　███▉ █▎\n　◢████◣⌠ₘ℩\n　　██◥█◣\≫\n　　██　◥█◣\n　　█▉　　█▊\n　　█▊　　█▊\n　　█▊　　█▋\n　　 █▏　　█▙\n　　 █ \nだからよ...止まるじゃねえぞ')
    await util.silence(session.ctx, 30)
    
@sv.on_command('不要停下来啊', aliases=('悼念'), only_to_me=False)
async def chat_daonian(session):
        await session.send(R.img('不要停下来啊.jpg').cqcode)
        
@sv.on_command('我要强奸你', aliases=('我要强奸露比', ), only_to_me=False)
async def ddhaole(session):
        await session.send('小心我把你婊子妈的子宫摘下来套你头上然后把你的鸡儿用液压钳剪掉哦~', at_sender=True)
        await util.silence(session.ctx, 60*5)

@sv.on_command('贴贴', only_to_me=True)
async def chat_mua(session):
    await session.send('呜嘿，贴贴~', at_sender=True)
        
@sv.on_command('贴贴贴贴', only_to_me=False)
async def chat_mua(session):
    await session.send('是找我贴贴吗！', at_sender=True)

# ============================================ #

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战', '刀'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)
