from io import BytesIO
import os
import requests
from PIL import Image
from hoshino import NoneBot, CommandSession
from hoshino.service import Service
import matplotlib.pyplot as plt
from .data_source import add_text,get_apikey
import base64
import time
import aiohttp

yobot_url = 'http://yobot2.bmfnfx.cn' #请填入你的yobot公网ip:端口或域名:端口
sv = Service('retire')
constellation_set = {'1':'射手','2':'摩羯','3':'水瓶','4':'双鱼','5':'白羊','6':'金牛','7':'双子','8':'巨蟹','9':'狮子','10':'处女','11':'天秤','12':'天蝎'}
time = time.localtime(time.time())
month = str(time.tm_mon)
year = str(time.tm_year)
constellation = constellation_set[month]

@sv.on_command('离职报告', aliases=('生成离职报告','生成报告'), only_to_me=False)
async def create_resignation_report(session:CommandSession):
    uid = session.ctx['user_id']
    nickname = session.ctx['sender']['nickname']
    gid = session.ctx['group_id']
    apikey = get_apikey(gid)
    url = f'{yobot_url}/yobot/clan/{gid}/statistics/api/?apikey={apikey}'
    aiosession = aiohttp.ClientSession()
    async with aiosession.get(url, timeout=5) as resp:
        data = await resp.json()
        clanname = data['groupinfo'][0]['group_name']
        challenges: list = data['challenges']
        continue_chl = []
        miss_chl = []

        #筛选出出刀
        for chl in challenges[::-1]:
            if chl['qqid'] != uid:
                challenges.remove(chl)
        
        #筛选补偿刀和吞刀
        for chl in challenges:
            if chl['is_continue']:
                continue_chl.append(chl)
            if chl['damage'] == 0:
                miss_chl.append(chl)

        #总刀数 = 报刀数 - 补偿刀
        total_chl_num = len(challenges) - len(continue_chl)

        damage_to_boss: list = [0 for i in range(5)]
        total_damage = 0
        for chl in challenges:
            damage_to_boss[chl['boss_num']-1] += chl['damage']
            total_damage += chl['damage']
        avg_day_damage = int(total_damage/6)
    
    #设置中文字体
    plt.rcParams['font.family'] = ['Microsoft YaHei']
    plt.figure(figsize=(4, 4))
    labels = [f'{x+1}王' for x in range(0,5) if damage_to_boss[x] != 0]
    sizes = [x for x in damage_to_boss if x != 0]
    patches, l_text, p_text = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,labeldistance=1.1)
    for t in l_text:
        #为标签设置字体大小
        t.set_size(15)
    for t in p_text:
        #为比例设置字体大小
        t.set_size(15)
    buf = BytesIO()
    plt.savefig(buf, format='png', transparent=True, dpi=120)
    pie_img = Image.open(buf)

    #清空饼图
    plt.clf()

    x = [f'{x}王' for x in range(1,6)]
    y = damage_to_boss
    plt.figure(figsize=(4.5,2.7))   #柱状图的宽和高，单位：英寸
    ax = plt.axes()

    #设置标签大小
    plt.tick_params(labelsize=15)   #底部x王标签字样的大小

    #设置y轴不显示刻度
    plt.yticks([])


    #绘制柱状图
    recs = ax.bar(x,y,width=0.618)  #width是柱子的粗细参数

    #删除边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #设置数量显示
    for i in range(0,5):
        rec = recs[i]
        h = rec.get_height()
        plt.text(rec.get_x()-0.1, h*1.05, f'{int(damage_to_boss[i]/10000)}万',fontdict={"size":15})
        #前两个参数是柱子数值数字的位置，最后一个size是这些数字的大小

    buf = BytesIO()
    plt.savefig(buf, format='png', transparent=True, dpi=120)
    plt.close()
    bar_img = Image.open(buf)

    #将饼图和柱状图粘贴到模板图,mask参数控制alpha通道，括号的数值对是偏移的坐标
    current_folder = os.path.dirname(__file__)
    img = Image.open(os.path.join(current_folder,'公会离职报告模板.jpg'))
    img.paste(pie_img, (605,880), mask=pie_img.split()[3])  #饼图的位置
    img.paste(bar_img, (125,960), mask=bar_img.split()[3])  #柱状图的位置

    #添加文字到img
    row1 = f'''
    {total_chl_num}

    {18-total_chl_num}

    {total_damage}
    '''
    row2 = f'''
    {round(total_chl_num/18*100,2)}%

    {len(miss_chl)}

    {avg_day_damage}
    '''
    
    add_text(img, row1, position=(395,628), textsize=35)
    add_text(img, row2, position=(850,628), textsize=35)
    add_text(img, year, position=(355,450), textsize=40)
    add_text(img, month, position=(565,450), textsize=40)
    add_text(img, constellation, position=(710,450), textsize=40)
    if len(clanname) <= 7:
        add_text(img, clanname, position=(300+(7-len(clanname))/2*40, 520), textsize=40)
    else:
        add_text(img, clanname, position=(300+(10-len(clanname))/2*30, 525), textsize=30)
    add_text(img, nickname, position=(180,372), textsize=40)

    #输出
    buf = BytesIO()
    img.save(buf,format='JPEG')
    base64_str = f'base64://{base64.b64encode(buf.getvalue()).decode()}'
    await session.send(f'[CQ:image,file={base64_str}]', at_sender=True)