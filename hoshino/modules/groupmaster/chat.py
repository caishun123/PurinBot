import random

from nonebot import on_command

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')


sv = Service('chat', visible=False)

@sv.on_fullmatch('沙雕机器人')
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')

@sv.on_fullmatch(('老公'), only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '你给我滚！', at_sender=True)
    
@sv.on_fullmatch(('我喜欢你','我爱你', '亲亲'), only_to_me=True)
async def chat_suki(bot, ev):
    await bot.send(ev, '诶嘿嘿，mua~', at_sender=True)

@sv.on_fullmatch(('mua'), only_to_me=True)
async def chat_mua(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, '変態不審者ですか？', at_sender=True)
        #await bot.send(ev, R.rec('nzzsm_xcw.m4a').cqcode)
    else:
        await bot.send(ev, '笨蛋~', at_sender=True)

@sv.on_fullmatch('我有个朋友说他好了', '我朋友说他好了')
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    await util.silence(ev, 30)


@sv.on_fullmatch('所有的努力全部木大', only_to_me=False)
async def nihaole(bot, ev):
    await bot.send(ev, '不要停下来啊！\nₘₙⁿ\n▏n\n█▏　､⺍\n█▏ ⺰ʷʷｨ\n█◣▄██◣\n◥██████▋\n　◥████ █▎\n　　███▉ █▎\n　◢████◣⌠ₘ℩\n　　██◥█◣\≫\n　　██　◥█◣\n　　█▉　　█▊\n　　█▊　　█▊\n　　█▊　　█▋\n　　 █▏　　█▙\n　　 █ \nだからよ...止まるじゃねえぞ')
    await util.silence(ev, 30)
    
@sv.on_fullmatch(('不要停下来啊','悼念'), only_to_me=False)
async def chat_daonian(bot, ev):
        await bot.send(ev, R.img('不要停下来啊.jpg').cqcode)
        
@sv.on_fullmatch(('我要强奸你','我要强奸露比'), only_to_me=False)
async def ddhaole(bot, ev):
        await bot.send(ev, '小心我把你婊子妈的子宫摘下来套你头上然后把你的鸡儿用液压钳剪掉哦~', at_sender=True)
        await util.silence(ev, 60*5)

@sv.on_fullmatch(('贴贴'), only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '呜嘿，贴贴~', at_sender=True)
        
@sv.on_fullmatch(('贴贴贴贴'), only_to_me=False)
async def chat_mua(bot, ev):
    await bot.send(ev, '是找我贴贴吗！', at_sender=True)
    
@sv.on_fullmatch(('早上好','早安'), only_to_me=True)
async def chat_ohayou(bot, ev):
    await bot.send(ev, '早呀早呀~', at_sender=True)
    
@sv.on_fullmatch(('晚安','睡啦'), only_to_me=True)
async def chat_oysm(bot, ev):
    await bot.send(ev, '快去睡吧~做个好梦哟ww', at_sender=True)
    
@sv.on_fullmatch(('加油'),only_to_me=True)
async def chat_ganbare(bot, ev):
    await bot.send(ev, '嘿嘿~你也要加油啦~', at_sender=True)

@sv.on_fullmatch(('辛苦了','辛苦啦'), only_to_me=True)
async def chat_otkr(bot, ev):
    await bot.send(ev, '呜呜呜谢谢你QwQ', at_sender=True)
    
@sv.on_fullmatch(('想你了','想你啦'), only_to_me=True)
async def chat_miss(bot, ev):
    await bot.send(ev, '我也...一直很想你呢w', at_sender=True)

@sv.on_fullmatch(('今天天气不错呢','天气真好'), only_to_me=False)
async def chat_tkgii(bot, ev):
    await bot.send(ev, '对呀对呀，好想和你一起出门玩呢~', at_sender=True)
    
@sv.on_fullmatch(('下雨了','打雷了'), only_to_me=False)
async def chat_ame(bot, ev):
    await bot.send(ev, '呜呜呜呜呜我好怕打雷啊QwQ', at_sender=True)

@sv.on_fullmatch(('别怕','别怕我在','有我在呢','我在呢','我陪你','我会陪你','我会陪你的'), only_to_me=True)
async def chat_djb(bot, ev):
    await bot.send(ev, '你在我身边的话...应该什么都会变好的吧~', at_sender=True)
    await bot.send(ev, '嗯~最————喜欢你啦！', at_sender=False)

@sv.on_fullmatch(('下班','下班啦','下班了'), only_to_me=False)
async def chat_xb(bot, ev):
    await bot.send(ev, '哦吼！今天辛苦啦~', at_sender=True)

@sv.on_fullmatch(('又熬夜了？'), only_to_me=True)
async def chat_nosleep(bot, ev):
    await bot.send(ev, R.img('又熬夜了.jpg').cqcode)
    
@sv.on_fullmatch(('我醒啦'), only_to_me=False)
async def chat_nxl(bot, ev):
    await bot.send(ev, '你醒啦 给你留了头狂暴牛', at_sender=True)
    
@sv.on_fullmatch(('Box管理','box管理','BOX管理','boxmgr','BoxMgr','BoxManager'), only_to_me=False)
async def box_mgr(bot, ev):
    await bot.send(ev, '\nBox在线录入管理\nhttps://w.url.cn/s/AmE3Fmg', at_sender=True)

@sv.on_fullmatch(('自助购买','续费Bot','续费bot','Bot续费','bot续费','purinshop'), only_to_me=False)
async def box_shop(bot, ev):
    await bot.send(ev, '\nBot自助购买续费食用指北\n自助续费购买的地址在链接里面\nhttps://purinbot.bmfnfx.cn/help-purinshop/', at_sender=True)

@sv.on_fullmatch(('官网','网站','主页','website'), only_to_me=True)
async def bot_website(bot, ev):
    await bot.send(ev, '\nPurinBot官网\nhttps://w.url.cn/s/Aj7FzfS', at_sender=True)

# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

@sv.on_keyword(('网抑云','黑化','生而为人'))
async def chat_wyy(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('网抑云.jpg').cqcode)

@sv.on_keyword(('色图','涩图'))
async def chat_sepi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('sepi.png').cqcode)

@sv.on_keyword(('天气'))
async def chat_tenki(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, "天気と言えば...天気がいいから、散歩しましょう。（笑）", at_sender=False)

nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)
