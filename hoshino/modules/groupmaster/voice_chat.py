import random
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

sv = Service('voice-chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('这个可以有', only_to_me=False)
async def yrmsn(session):
    await session.send(R.rec('yarimasuna_maho.m4a').cqcode, at_sender=False)

@sv.on_command('讲个鬼故事', aliases=('New Year Burst') ,only_to_me=False)
async def nyb(session):
    await session.send(R.rec('new_year_burst.m4a').cqcode, at_sender=False)
    
@sv.on_command('萝莉喷水', aliases=('xcw喷水','小仓唯喷水') ,only_to_me=False)
async def xcwub(session):
    await session.send(R.rec('ub_xcw.m4a').cqcode, at_sender=False)
    
@sv.on_command('咕噜灵波', aliases=('咕噜灵波~') ,only_to_me=False)
async def kllp(session):
    await session.send(R.rec('kururinpa_maho.m4a').cqcode, at_sender=False)
    
@sv.on_command('炼铜', aliases=('恋童','炼','铜','色图','涩图','瑟图') ,only_to_me=False)
async def lt(session):
    i = random.randint(1,2)
    if i == 1:
        await session.send(R.rec('yabarihentaisandesu_xcw.m4a').cqcode, at_sender=False)
    else:
        await session.send(R.rec('ayashihentai_xcw.m4a').cqcode, at_sender=False)

@sv.on_command('狼姐我爱你', aliases=('真琴我爱你') ,only_to_me=False)
async def ueokrrr(session):
    await session.send(R.rec('ueokorareru_makoto.m4a').cqcode, at_sender=False)

