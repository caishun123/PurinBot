from hoshino import util
from hoshino.util import FreqLimiter
from hoshino.service import Service
from nonebot import on_command
import requests,json

sv = Service('clanbattle-query', enable_on_default=True)

_lmt = FreqLimiter(2)

@sv.on_command('会战排名查询', aliases=('会战查询', '会战排名'), only_to_me=False)
async def clanbattle_query_menu(session):
	msg = f'\n公会战排名查询-API By @Kengxxiao\n请选择查询方式：\n>>>按公会名查询：公会查询 公会名 | cbqn 公会名\n>>>按会长名查询：会长查询 会长名字 | cbqm 会长名字\n>>>按排名查询：排名查询 名次 | cbqr 名次\n>>>按分数查询：分数查询 | cbqs 分数\n>>>当前档线查询：查档 | cbql\nTips："|"前后为命令的两种写法，可以任意选择一种使用~\n例如："公会查询 北宇治"与"cbqn 北宇治"效果相同\n公会名查询和会长名查询支持正则表达式哦~'
	await session.send(msg, at_sender=True)


@sv.on_command('公会查询', aliases=('cbqn'), only_to_me=False)
async def clanbattle_query_clanname(session):
	uid = session.ctx['user_id']
	if not _lmt.check(uid):
		await session.send('查询得太快了哦，请稍等一会儿~', at_sender=True)
		return
	_lmt.start_cd(uid)
	clan_name = util.normalize_str(session.current_arg_text)
	url = "https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com//name/0"
	name = json.dumps({ "clanName": clan_name })
	headers = {'Accept': 'application/json, text/javascript, */*; q=0.01','Custom-Source': 'PurinBot','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Content-Type': 'application/json','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com','Content-Length': '33','Pragma': 'no-cache','Cache-Control': 'no-cache','Origin': 'https://kyouka.kengxxiao.com','Referer': 'https://kyouka.kengxxiao.com/'}
	r = requests.post(url,data=name,headers=headers,timeout=10)
	if r.status_code == requests.codes.ok:
		r_dec = json.loads(r.text)
		if not r_dec['data']:
			msg = f"您所查询的公会尚未参加公会战或排名超出统计范围OxO"
			await session.send(msg, at_sender=True)
			return
		else:
			full = r_dec['full']
			enter = '================='
			if full > 10:
				msg = [f'\n下次查询将在5分钟后可用~\n共为您查询到{full}条结果，最多显示10条，请缩小搜索范围哦:']
			else:
				msg = [f'\n下次查询将在5分钟后可用~\n共为您查询到{full}条结果:']
			for data in r_dec['data'][0:10]:
				msg.append(
					f'行会名：{data["clan_name"]}\n行会人数：{data["member_num"]}\n行会会长：{data["leader_name"]}\n当前排名：{data["rank"]}\n当前伤害：{data["damage"]}')
			_lmt.start_cd(uid, 300)
			await session.send(f'\n{enter}\n'.join(msg), at_sender=True)
	else:
		await session.send('查询出错，接口可能访问过大或维护，休息一会再试吧QwQ', at_sender=True)
		uid = session.ctx['user_id']
		_lmt.start_cd(uid, 150)

@on_command('档线查询',aliases=('查询档线','cbql'), only_to_me=False)
async def rank_search(session):
	uid = session.ctx['user_id']
	if not _lmt.check(uid):
		await session.send('查询得太快了哦，请稍等一会儿~', at_sender=True)
		return
	_lmt.start_cd(uid)
	
	url = "https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/line"
	data = json.dumps({"history":0})
	headers = {'Accept': 'application/json, text/javascript, */*; q=0.01','Custom-Source': 'PurinBot','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Content-Type': 'application/json','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com','Content-Length': '33','Pragma': 'no-cache','Cache-Control': 'no-cache','Origin': 'https://kyouka.kengxxiao.com','Referer': 'https://kyouka.kengxxiao.com/'}
	r = requests.post(url,headers=headers,data=data,timeout=10)
	if r.status_code == requests.codes.ok:
		r_dec = json.loads(r.text)
		enter = '================='
		msg = [f'\n下次查询将在5分钟后可用~\n以下是查询结果:']
		for data in r_dec['data'][0:10]:
				msg.append(
					f'行会名：{data["clan_name"]}\n行会人数：{data["member_num"]}\n行会会长：{data["leader_name"]}\n当前排名：{data["rank"]}\n当前伤害：{data["damage"]}')
		_lmt.start_cd(uid, 300)
		await session.send(f'\n{enter}\n'.join(msg), at_sender=True)
	else:
		await session.send('查询出错，接口可能访问过大或维护，休息一会再试吧QwQ', at_sender=True)
		uid = session.ctx['user_id']
		_lmt.start_cd(uid, 150)

@on_command('排名查询',aliases=('cbqr'), only_to_me=False)
async def clanbattle_query_rank(session):
	uid = session.ctx['user_id']
	if not _lmt.check(uid):
		await session.send('查询得太快了哦，请稍等一会儿~', at_sender=True)
		return
	_lmt.start_cd(uid)

	rank = util.normalize_str(session.current_arg_text)
	data = json.dumps({"history":0})
	url = "https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/rank/"+f"{rank}"
	headers = {'Accept': 'application/json, text/javascript, */*; q=0.01','Custom-Source': 'PurinBot','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Content-Type': 'application/json','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com','Content-Length': '33','Pragma': 'no-cache','Cache-Control': 'no-cache','Origin': 'https://kyouka.kengxxiao.com','Referer': 'https://kyouka.kengxxiao.com/'}
	r = requests.post(url,headers=headers,data=data,timeout=10)
	if r.status_code == requests.codes.ok:
		r_dec = json.loads(r.text)
		enter = '================='
		msg = [f'\n下次查询将在5分钟后可用~\n以下是查询结果:']
		for data in r_dec['data'][0:10]:
				msg.append(
					f'行会名：{data["clan_name"]}\n行会人数：{data["member_num"]}\n行会会长：{data["leader_name"]}\n当前排名：{data["rank"]}\n当前伤害：{data["damage"]}')
		_lmt.start_cd(uid, 300)
		await session.send(f'\n{enter}\n'.join(msg), at_sender=True)
	else:
		await session.send('查询出错，接口可能访问过大或维护，休息一会再试吧QwQ', at_sender=True)
		uid = session.ctx['user_id']
		_lmt.start_cd(uid, 150)

@sv.on_command('会长查询', aliases=('cbqm'), only_to_me=False)
async def clanbattle_query_leadername(session):
	uid = session.ctx['user_id']
	if not _lmt.check(uid):
		await session.send('查询得太快了哦，请稍等一会儿~', at_sender=True)
		return
	_lmt.start_cd(uid)
	leader_name = util.normalize_str(session.current_arg_text)
	url = "https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/leader/0"
	name = json.dumps({ "leaderName": leader_name })
	headers = {'Accept': 'application/json, text/javascript, */*; q=0.01','Custom-Source': 'PurinBot','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Content-Type': 'application/json','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com','Content-Length': '33','Pragma': 'no-cache','Cache-Control': 'no-cache','Origin': 'https://kyouka.kengxxiao.com','Referer': 'https://kyouka.kengxxiao.com/'}
	r = requests.post(url,data=name,headers=headers,timeout=10)
	if r.status_code == requests.codes.ok:
		r_dec = json.loads(r.text)
		if not r_dec['data']:
			msg = f"您所查询的公会尚未参加公会战或排名超出统计范围OxO"
			await session.send(msg, at_sender=True)
			return
		else:
			full = r_dec['full']
			enter = '================='
			if full > 10:
				msg = [f'\n下次查询将在5分钟后可用~\n共为您查询到{full}条结果，最多显示10条，请缩小搜索范围哦:']
			else:
				msg = [f'\n下次查询将在5分钟后可用~\n共为您查询到{full}条结果:']
			for data in r_dec['data'][0:10]:
				msg.append(
					f'行会名：{data["clan_name"]}\n行会人数：{data["member_num"]}\n行会会长：{data["leader_name"]}\n当前排名：{data["rank"]}\n当前伤害：{data["damage"]}')
			_lmt.start_cd(uid, 300)
			await session.send(f'\n{enter}\n'.join(msg), at_sender=True)
	else:
		await session.send('查询出错，接口可能访问过大或维护，休息一会再试吧QwQ', at_sender=True)
		uid = session.ctx['user_id']
		_lmt.start_cd(uid, 150)

@on_command('分数查询',aliases=('cbqs'), only_to_me=False)
async def clanbattle_query_score(session):
	uid = session.ctx['user_id']
	if not _lmt.check(uid):
		await session.send('查询得太快了哦，请稍等一会儿~', at_sender=True)
		return
	_lmt.start_cd(uid)

	score = int(session.current_arg_text) - 1
	data = json.dumps({"history":0})
	url = "https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/score/"+f"{score}"
	headers = {'Accept': 'application/json, text/javascript, */*; q=0.01','Custom-Source': 'PurinBot','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Content-Type': 'application/json','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com','Content-Length': '33','Pragma': 'no-cache','Cache-Control': 'no-cache','Origin': 'https://kyouka.kengxxiao.com','Referer': 'https://kyouka.kengxxiao.com/'}
	r = requests.post(url,headers=headers,data=data,timeout=10)
	if r.status_code == requests.codes.ok:
		r_dec = json.loads(r.text)
		enter = '================='
		msg = [f'\n下次查询将在5分钟后可用~\n以下是查询结果:']
		for data in r_dec['data'][0:10]:
				msg.append(
					f'行会名：{data["clan_name"]}\n行会人数：{data["member_num"]}\n行会会长：{data["leader_name"]}\n当前排名：{data["rank"]}\n当前伤害：{data["damage"]}')
		_lmt.start_cd(uid, 300)
		await session.send(f'\n{enter}\n'.join(msg), at_sender=True)
	else:
		await session.send('查询出错，接口可能访问过大或维护，休息一会再试吧QwQ', at_sender=True)
		uid = session.ctx['user_id']
		_lmt.start_cd(uid, 150)