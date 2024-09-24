import time

import wxauto

nowtime = time.localtime()
print(nowtime)
print(f'现在时间为：{nowtime[0]}年{nowtime[1]}月{nowtime[2]}日{nowtime[3]}点{nowtime[4]}分{nowtime[5]}秒\n详情：目前是{nowtime[0]}中的第{nowtime[-2]}天')

def get_wanttime():
    a = ['年份year','月份month','日day','时','分','秒']
    team = []
    z = time.localtime()
    for i in range(len(a)):
        while True:
            try:
                WantTime = int(input(f'{a[i]}:'))
            except:
                print('错误:请输入数字！！！')
            else:
                if WantTime < z[i]:
                    if a[i] == '秒':
                        break
                    else:
                        print('时间不能小于当前（时间无法倒流^_^）')
                else:
                    break
        team.append(WantTime)
    return team

def get_how():
    name = input('请输入联系人名称:')
    what = input('你要发送的信息：')
    return name,what

def spend(name,time_get,what):
    while True:
        z = time.localtime()
        geee = [z[0],z[1],z[2],z[3],z[4],z[5]]
        print(geee)
        print(time_get)
        print('====='*12)
        if geee == time_get:
            wx = wxauto.WeChat()
            wx.SendMsg(msg=what,who=how)
            print('===='*12)
            print(f'已发送至"{name}"群聊或联系人，信息为：{what}')
            time.sleep(2)
            break
    print('已完成')

if __name__ == '__main__':
    while True:
        want_time = get_wanttime()
        how,what = get_how()
        print(f'请确定信息,发送信息为：',end='')
        ki = ['年份year', '月份month', '日day', '时', '分', '秒']
        for i in range(len(want_time)):
            print(f'{ki[i]}: {i}',end='    ')
        print(f'\n发送的信息为:   {what}')
        get_data = input('确定:true;否定:false;默认为启动')
        if get_data == 'false':
            pass
        else:
            spend(how, want_time,what)
            break