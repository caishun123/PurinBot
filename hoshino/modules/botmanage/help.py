from hoshino import Service, Privilege as Priv

sv = Service('_help_', manage_priv=Priv.SUPERUSER, visible=False)

MANUAL = '''
=====================
- 枫使用说明(1/2) -
=====================
- 公主连接Re:Dive -
==================
[运势] 看看你今天的运气怎么样~文本和创意来自@BillYang2016的PCR黄历插件
[会战帮助] 查看会战相关指令帮助
[Box管理] 网页端录入管理公会成员Box
[离职报告] 生成当期会战离职报告
[会战查询] 查询国服会战数据，30分钟更新一次，接口由@Kengxxiao提供
[@bot来发十连] 十连转蛋模拟
[@bot来发单抽] 单抽转蛋模拟
[@bot来一井] 4w5钻！买定离手！
[.布丁ub3] 查询角色ub语音，格式为[.角色ub(1~6)] 括号里的数字代表ub语音序号，不用填括号，不填数字默认随机。
[.ubr] 随机查询一个角色的ub语音，别漏了点哦~
[竞技场查询 布丁 空花 黑骑 望 咕噜灵波]竞技场查询，接口由pcrdfans.com提供
[@bot妈] 给主さま盖章章
[rank表] 查看rank推荐表
[黄骑充电表] 查询黄骑1动充电规律
[@bot官漫132] 官方四格阅览
[谁是春黑] 别称查询角色
[wiki查询] BcrWiki查询菜单
[挖矿 15001] 查询矿场中还剩多少钻
[工资 1919] 查询今日竞技场结算钻石数
[切噜一下] 后以空格隔开接想要转换为切噜语的话
[切噜～♪切啰巴切拉切蹦切蹦] 切噜语翻译
===========
发送 帮助2 进行翻页
※※Powered By HoshinoBot※※
'''.strip()


MANUAL2 = '''
=====================
- 枫使用说明(2/2) -
===========
- 通用功能 -
===========
[@bot网抑云] 上号！网抑云启动！评论接口由酷Q用户@wzt123提供
[搜无损 星をつなげて] 搜索无损FLAC音乐，数据由acgjc.com提供
[.r] 掷骰子
[.r 3d12] 掷3次12面骰子
[@bot精致睡眠] 8小时精致睡眠(bot需具有群管理权限)
[给我来一份精致昏睡下午茶套餐] 叫一杯先辈特调红茶(bot需具有群管理权限)
[@bot来杯咖啡] 联系维护组，空格后接反馈内容
[#查询授权] 查询Bot在本群的到期时间
[自助购买] Bot自助续费以及新购
==========
- 群管理限定功能 -
=================
[翻译 もう一度、キミとつながる物語] 机器翻译
[lssv] 查看功能模块的开关状态
[禁用 pcr-arena-reminder-tw] 禁用背刺时间提醒(UTC+8)（群管理及以上可用）
[禁用 exp-reminder] 禁用经验药水购买提醒（群管理及以上可用）
[禁用 hourcall] 禁用时报（群管理及以上可用）
[大家问xxx你答yyy] 管理员调教bot答复，群内通用
[不要回答xxx] 删除调教的问题，xxx是问题而不是回答内容
=====================================
发送 帮助1 进行翻页
※※Powered By HoshinoBot※※
'''.strip()

wiki = '''
======================
-公主连结国服Wiki查询-
======================
[查询角色#镜华] 查询角色信息
[查询装备#冰之大剑] 查询装备信息
>>>国服Wiki仅包含B服数据<<<
===========
'''.strip()

cbhelp = '''
公会战手册页面 https://w.url.cn/s/ACg7k88
公会战指令页面 https://w.url.cn/s/Akrwy93
[离职报告] 生成当期会战离职报告
[Box管理] 网页端录入管理公会成员Box
'''.strip()


@sv.on_command('help', aliases=('manual', '帮助', '说明', '使用说明', '幫助', '說明', '使用說明', '菜单', '菜單', 'manual1', '帮助1', '说明1', '使用说明1', '幫助1', '說明1', '使用說明1', '菜单1', '菜單1', 'help1'), only_to_me=False)
async def send_help(session):
    await session.send(MANUAL)

@sv.on_command('help2', aliases=('manual2', '帮助2', '说明2', '使用说明2', '幫助2', '說明2', '使用說明2', '菜单2', '菜單2'), only_to_me=False)
async def send_help(session):
    await session.send(MANUAL2)
    
@sv.on_command('wiki查询', aliases=('Wiki查询','WIKI查询'), only_to_me=False)
async def send_help(session):
    await session.send(wiki)
    
@sv.on_command('会战帮助', aliases=('！help','!help','!帮助','！帮助'), only_to_me=False)
async def send_help(session):
    await session.send(cbhelp)