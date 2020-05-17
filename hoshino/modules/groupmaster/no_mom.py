#得去写一个service，clean_blacklist_user，直接把开启功能的崽种拽出黑名单
import random
import re

from hoshino import logger, util, Service, R, Privilege

sv = Service('no-mom', enable_on_default=False, visible=True)

@sv.on_rex(re.compile(r'rbq|RBQ|憨批|废物|死妈|崽种|傻逼|傻逼玩意|没用东西|傻B|傻b|SB|sb|煞笔|cnm|爬|kkp|nmsl|D区|口区|我是你爹|nmbiss|弱智|给爷爬|杂种爬|你妈死了|杂种|叼毛|露逼|露屄|草泥马|操你妈|草你妈|婊子|死了|撒了你|杀了'), normalize=True)#正则匹配素质文本

async def no_mom(bot, ctx, match):
    user_id = ctx['user_id']
    msg_from = str(user_id)
    if ctx['message_type'] == 'group':
        msg_from += f'@[群:{ctx["group_id"]}]'
    elif ctx['message_type'] == 'discuss':
        msg_from += f'@[讨论组:{ctx["discuss_id"]}]'
    logger.critical(f'Self: {ctx["self_id"]}, Message {ctx["message_id"]} from {msg_from}: {ctx["message"]}')
    msg = random.choice(open('/home/ubuntu/HoshinoBot/res/img/nmsl.txt').readlines())#这里填写你喷词文本的绝对路径
    await bot.send(ctx, msg)