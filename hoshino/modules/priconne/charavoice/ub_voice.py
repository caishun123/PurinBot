from hoshino.util import FreqLimiter
from ..chara import Chara
from . import sv
from hoshino.res import R
import os
from os import path
import random

@sv.on_rex(r'^\.\s*(.{1,20})ub(1|2|3|4|5|6)?$', normalize=False)
async def ubvoice(bot, ctx, match):
    name = match.group(1)
    ub_num = match.group(2)
    if ub_num is None:
        ub_num = random.randint(1,6)
    else:
        ub_num = int(ub_num)
    chara = Chara.fromname(name, star=0)
    chara_id = chara.id
    if chara.id == Chara.UNKNOWN:
        await bot.send(ctx, f'兰德索尔似乎没有叫"{name}"的人，请换个人物查询', at_sender=True)
        return
    if os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{chara_id}/ub_{ub_num}00.m4a'):
        msg = R.rec(f'{chara_id}/ub_{ub_num}00.m4a').cqcode
        await bot.send(ctx, msg, at_sender=False)
    else:
        while not os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{chara_id}/ub_{ub_num}00.m4a') and ub_num >= 0:
            if not os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{chara_id}/ub_{ub_num}00.m4a') and ub_num == 0:
                await bot.send(ctx, '暂时没有查询到对应语音，请等待Bot维护人员更新语音资源。', at_sender=True)
                ub_num = ub_num - 1
                break
            else:
                ub_num = ub_num - 1

        msg = R.rec(f'{chara_id}/ub_{ub_num}00.m4a').cqcode
        await bot.send(ctx, msg, at_sender=False)
        

@sv.on_rex(r'^(\.ubr|\.ubrand|.ub随机)$', normalize=False)
async def randubvoice(bot, ctx, match):
    rand_id = random.randint(1001,1127)
    rand_num = random.randint(1,6)
    while rand_id == Chara.UNKNOWN:
        v = random.randint(1,5)
        rand_id = rand_id - v
        if rand_id <= 1000:
            rand_id = 1099
        
    if os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{rand_id}/ub_{rand_num}00.m4a'):
        msg = R.rec(f'{rand_id}/ub_{rand_num}00.m4a').cqcode
        await bot.send(ctx, msg, at_sender=False)
    else:
        while not os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{rand_id}/ub_{rand_num}00.m4a') and rand_num >= 0:
            if not os.path.isfile(f'/home/ubuntu/HoshinoBot/res/img/record/{rand_id}/ub_{rand_num}00.m4a') and rand_num == 0:
                await bot.send(ctx, '运气不是很好呢QwQ再发一遍吧~', at_sender=True)
                rand_num = rand_num - 1
                break
            else:
                rand_num = rand_num - 1

        msg = R.rec(f'{rand_id}/ub_{rand_num}00.m4a').cqcode
        await bot.send(ctx, msg, at_sender=False)