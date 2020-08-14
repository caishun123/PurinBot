import random
import time
from hoshino import Service, R, util
from hoshino.util import DailyNumberLimiter

sv = Service('pcr-fortune')

lmt = DailyNumberLimiter(1)

@sv.on_command('运势', aliases=('黄历','黄历查询','运势查询','今日运势'), only_to_me=False)
async def today_fortune(session):
    await session.send('请输入“运势+任意数字(1~100)”查询今日运势哦~', at_sender=True)

@sv.on_rex(r'^运势([1-9]\d?|100)$', normalize=True)
async def today_fortune_query(bot, event):
    uid = event['user_id']
    if not lmt.check(uid):
        await bot.send(event, '今天已经查过运势了哦，请明天再来吧~', at_sender=True)
        return
    lmt.increase(uid)
    
    config = util.load_config(__file__)
    
    gacha_hour = random.randint(0,24)
    gacha_min = random.randint(0,60)
    gacha_sec = random.randint(0,60)
    gachatime = f'{gacha_hour}时{gacha_min}分{gacha_sec}秒'
    
    hournow = time.localtime().tm_hour
    timenow = time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time()))
    
    characters = random.choice(config["characters"])
    position = random.choice(config["position"])
    actions = random.choice(config["actions"])
    
    inputnum = int(event.match.group(1))
    flag = random.randint(1,100)
    diff = abs(inputnum - flag)
    if 0< diff <= 16:
        fortune = '大吉'
    elif 16 < diff <= 33:
        fortune = '中吉'
    elif 33 < diff <= 50:
        fortune = '小吉'
    elif 50 < diff <= 67:
        fortune = '小凶'
    elif 67 < diff <= 84:
        fortune = '凶'
    elif 84 < diff <= 99:
        fortune = '大凶' 

    all_things = ['gacha','arena','mainmap','story','clanbattle','hard']
    things = random.sample(all_things,2)
    suitable_thing = things[0]
    unsuitable_thing = things[1]
    
    suitable = config["suitable"][suitable_thing]
    unsuitable = config["unsuitable"][unsuitable_thing]
    
    msg = f'\n今日运势：{fortune}\n当前时间：{timenow}\n今日幸运角色：{characters}\n宜{suitable}\n忌{unsuitable}\n抽卡加成时间：{gachatime}\n抽卡加成方向：{position}\n抽卡加成动作：{actions}\n'
    await bot.send(event, msg, at_sender=True)