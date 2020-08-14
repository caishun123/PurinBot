import nonebot
from hoshino.service import Service
from hoshino import R

sv = Service('exp-reminder', enable_on_default=True)

@sv.scheduled_job('cron', hour='*/6')
async def exp_reminder():
    pic = R.img('exp_reminder.jpg').cqcode
    msgs = f'骑士君，该上线买经验药水啦~\n{pic}'
    await sv.broadcast(msgs, 'exp_reminder', 0.2)