"""
无损音乐搜索 数据来自acgjc.com
"""
import requests

from hoshino import Service, Privilege, CommandSession, logger
from urllib.parse import quote
from hoshino.util import FreqLimiter

sv = Service('flac', manage_priv=Privilege.SUPERUSER, enable_on_default=True, visible=True)

_lmt = FreqLimiter(2)

@sv.on_command('搜无损', aliases=('查无损','搜歌'), only_to_me=False)
async def search_flac(session: CommandSession):
    uid = session.ctx['user_id']
    if not _lmt.check(uid):
        await session.send('查询的太快了哦，两次查询间隔为90秒~', at_sender=True)
        return
    #_lmt.start_cd(uid)
    
    keyword = session.current_arg_text
    resp = requests.get('http://mtage.top:8099/acg-music/search', params={'title-keyword': keyword}, timeout=1)
    res = resp.json()
    if res['success'] is False:
        logger.error(f"Flac query failed.\nerrorCode={res['errorCode']}\nerrorMsg={res['errorMsg']}")
        session.finish(f'查询失败 请至acgjc官网查询 http://www.acgjc.com/?s={quote(keyword)}', at_sender=True)

    _lmt.start_cd(uid, 90)
    music_list = res['result']['content']
    music_list = music_list[:min(5, len(music_list))]

    details = [" ".join([
        f"{ele['title']}",
        f"{ele['downloadLink']}",
        f"密码：{ele['downloadPass']}" if ele['downloadPass'] else ""
    ]) for ele in music_list]

    msg = [
        f"共 {res['result']['totalElements']} 条结果" if len(music_list) > 0 else '没有任何结果',
        *details,
        '数据来自 http://www.acgjc.com',
        f'当前库内不包括acgjc的全部数据，更多结果可见 http://www.acgjc.com/?s={quote(keyword)}'
    ]

    session.finish('\n'.join(msg), at_sender=True)