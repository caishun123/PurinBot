from . import sv

@sv.on_command('arena_salary', aliases=('工资', 'jjc工资', '竞技场工资', 'jjc工资查询', '竞技场工资查询'))
async def arena_salary(session):
    rank = int(session.current_arg_text)
    salary = None
    if rank == 1:
        salary = 300
    elif rank == 2:
        salary = 250
    elif rank == 3:
        salary = 200
    elif rank == 4:
        salary = 175
    elif rank == 5:
        salary = 150
    elif rank == 6:
        salary = 145
    elif rank == 7:
        salary = 140
    elif rank == 8:
        salary = 135
    elif rank == 9:
        salary = 130
    elif rank > 9 and rank < 20:
        salary = 125
    elif rank > 19 and rank < 30:
        salary = 120
    elif rank > 29 and rank < 40:
        salary = 115
    elif rank > 39 and rank < 50:
        salary = 110
    elif rank > 49 and rank < 60:
        salary = 100
    elif rank > 59 and rank < 70:
        salary = 90
    elif rank > 69 and rank < 80:
        salary = 80
    elif rank > 79 and rank < 90:
        salary = 70
    elif rank > 89 and rank < 100:
        salary = 60
    elif rank > 99 and rank < 200:
        salary = 50
    elif rank > 199 and rank < 300:
        salary = 45
    elif rank > 299 and rank < 400:
        salary = 40
    elif rank > 399 and rank < 500:
        salary = 35    
    elif rank > 499 and rank < 1000:
        salary = 25    
    elif rank > 999 and rank < 5000:
        salary = 20   
    elif rank > 4999 and rank < 10000:
        salary = 15    
    elif rank > 9999 and rank < 12000:
        salary = 10    
    elif rank > 11999 and rank < 14000:
        salary = 5
    elif rank > 13999 and rank < 15000:
        salary = 4    
    elif rank > 14999 and rank < 30001:
        salary = 3   
    
    if salary is not None:
        msg = f"\n今日竞技场工资为{salary}钻石。 "
        await session.send(msg, at_sender=True)
    else:
        msg ="请重新输入1~30000范围内的数字进行查询。"
        await session.send(msg, at_sender=True)