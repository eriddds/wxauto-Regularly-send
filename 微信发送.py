import time
import wxauto
import PySimpleGUI as sg

nowtime = time.localtime()
print(nowtime)
print(f'现在时间为：{nowtime[0]}年{nowtime[1]}月{nowtime[2]}日{nowtime[3]}点{nowtime[4]}分{nowtime[5]}秒\n详情：目前是{nowtime[0]}中的第{nowtime[-2]}天')

def spend(name,time_get,what):
    while True:
        z = time.localtime()
        geee = [z[0],z[1],z[2],z[3],z[4],z[5]]
        print(time_get)
        print(geee)
        print('===='*12)
        if geee == time_get:
            wx = wxauto.WeChat()
            wx.SendMsg(msg=what,who=name)
            sg.Popup(f'已发送至"{name}"群聊或联系人，信息为：{what}',font=('黑体',20))
            break
    print('已完成')

def init_window0():
    layout1 = [
        [sg.B('中文', font=('黑体', 20)), sg.T('      '), sg.B('English', font=('黑体', 20))],
        [sg.B('定时发送', font=('黑体'), key='-2-')],
        [sg.B('自动回复', font=('黑体'), key='-3-')],
        [sg.B('信息轰炸', font=('黑体'), key='-4-')],
        # [sg.T(size=(40, 5)])
    ]
    window = sg.Window('微信自动程序', layout1)
    while True:
        event, values = window.read()
        print(values)
        if event == None:
            window.close()
            z = ''
            break
        if event == 'English':
            window['-2-'].update('Regularly send')
            window['-3-'].update('automatic reply')
            window['-4-'].update('Information bombardment')
        if event == '中文':
            window['-2-'].update('定时发送')
            window['-3-'].update('自动回复')
            window['-4-'].update('信息轰炸')
        if event == '-2-':
            window.close()
            nowtime = time.localtime()
            z = 'go one'
            break
        if event == '-3-':
            window.close()
            z = 'zd'
            break
        if event == '-4-':
            window.close()
            z = 'hz'
            break
    if z == 'go one':
        return 'two'
    elif z == 'zd':
        return 'three'
    elif z == 'hz':
        return 'four'
    else:
        return 'exit'


def init_window1():
    nowtime = time.localtime()
    text = f'{nowtime}\n现在时间为：{nowtime[0]}年{nowtime[1]}月{nowtime[2]}日{nowtime[3]}点{nowtime[4]}分{nowtime[5]}秒\n详情：目前是{nowtime[0]}中的第{nowtime[-2]}天'
    layout2 = [
        [sg.B('中文', font=('黑体', 20)), sg.T('      '), sg.B('English', font=('黑体', 20))],
        [sg.T(text=text, key='-tit-')],
        [sg.T(text='       请输入发送的时间        ', font=('黑体', 20), background_color='white', text_color='black',
              key='-title-')],
        [sg.T(text='')],
        [sg.T(text='年',key='-year-', font=('黑体', 20)), sg.In()],
        [sg.T(text='月',key='-mouth-', font=('黑体', 20)), sg.In()],
        [sg.T(text='日',key='-day-', font=('黑体', 20)), sg.In()],
        [sg.T(text='时',key='-hour-', font=('黑体', 20)), sg.In()],
        [sg.T(text='分',key='-min-', font=('黑体', 20)), sg.In()],
        [sg.T(text='秒',key='-sec-', font=('黑体', 20)), sg.In()],
        [sg.B('确认',key='-B1-'), sg.B('返回',key='-B2-')]
    ]
    window1 = sg.Window('定时发送', layout2)
    text = f'{nowtime}\n现在时间为：{nowtime[0]}年{nowtime[1]}月{nowtime[2]}日{nowtime[3]}点{nowtime[4]}分{nowtime[5]}秒\n详情：目前是{nowtime[0]}中的第{nowtime[-2]}天'
    while True:
        event, values = window1.read()
        if event == None:
            window1.close()
            z = 'exit'
            break
        if event == 'English':
            window1['-tit-'].update(f'{nowtime}\nnow time：{nowtime[0]}/{nowtime[1]}/{nowtime[2]}\n{nowtime[3]}:{nowtime[4]}:{nowtime[5]}sec  details：now is {nowtime[0]} day of {nowtime[-2]}')
            window1['-title-'].update('Please enter the sending time')
            window1['-year-'].update('year')
            window1['-mouth-'].update('mouth')
            window1['-day-'].update('day')
            window1['-hour-'].update('hour')
            window1['-min-'].update('min')
            window1['-sec-'].update('sec')
            window1['-B1-'].update('Confirm')
            window1['-B2-'].update('Return')
        if event == '中文':
            window1['-tit-'].update(f'{nowtime}\n现在时间为：{nowtime[0]}年{nowtime[1]}月{nowtime[2]}日{nowtime[3]}点{nowtime[4]}分{nowtime[5]}秒\n详情：目前是{nowtime[0]}中的第{nowtime[-2]}天')
            window1['-title-'].update('       请输入发送的时间        ')
            window1['-year-'].update('年')
            window1['-mouth-'].update('月')
            window1['-day-'].update('日')
            window1['-hour-'].update('时')
            window1['-min-'].update('分')
            window1['-sec-'].update('秒')
            window1['-B1-'].update('确认')
            window1['-B2-'].update('返回')
        if event == '-B2-':
            z = 'back'
            break
        if event == '-B1-':
            window1.close()
            z = 'set'
            break
    if z == 'back':
        window1.close()
        return 'one',None
    elif z == 'set':
        window1.close()
        text_data = []
        for i in range(len(values)):
            try:
                text_data.append(int(values[i]))
            except:
                sg.Popup('请输入数字\nplease enter a number')
                z = 'two'
                break
            else:
                pass
        if z == 'two':
            return 'two',None
        else:
            return 'set',text_data
    else:
        return 'exit',None

def winlog(time_get,what,name):
    layout3 = [
        [sg.T(text='请填写接收 联系人/群 名字（微信）:', font=('黑体', 15), key='-text-')],
        [sg.In()],
        [sg.B('确认', font=('黑体', 15), key='-button1-'), sg.B('取消', font=('黑体', 15), key='-button2-')]
    ]
    window = sg.Window('运行中', layout3)
    while True:
        z = time.localtime()
        geee = [z[0],z[1],z[2],z[3],z[4],z[5]]
        print(geee)
        print(time_get)
        print('====='*12)
        if geee == time_get:
            wx = wxauto.WeChat()
            wx.SendMsg(msg=what,who=name)
            print('===='*12)
            print(f'已发送至"{name}"群聊或联系人，信息为：{what}')
            sg.Popup('程序完成')
            time.sleep(2)
            break
def window_name(x):
    de = None
    layout3 = [
        [sg.B('中文', font=('黑体', 20)), sg.T('      '), sg.B('English', font=('黑体', 20))],
        [sg.T(text='请填写接收 联系人/群 名字（微信）:',font=('黑体',15),key='-text-')],
        [sg.In()],
        [sg.T(text='发送信息:',font=('黑体',15),key='-msg-'),sg.In()],
        [sg.B('确认',font=('黑体',15),key='-button1-'),sg.B('返回',font=('黑体',15),key='-button2-')]
    ]
    window = sg.Window('填写接收人',layout3)
    while True:
        event, values = window.read()
        if event == None:
            window.close()
            break
        if event == '-button2-':
            de = '1'
            window.close()
            break
        if event == '-button1-':
            window.close()
            de = '2'
            break
        if event == 'English':
            window['-text-'].update('Please fill in the recipient contact/group name (WeChat):')
            window['-msg-'].update('Message data:')
            window['-button1-'].update('confirm')
            window['-button2-'].update('return')
        if event == '中文':
            window['-text-'].update('请填写接收 联系人/群 名字（微信）:')
            window['-msg-'].update('发送信息:')
            window['-button1-'].update('确认')
            window['-button2-'].update('返回')
    if de == '1':
        return 'exit'
    if de == '2':
        spend(name=values[0],what=values[1],time_get=x)
def win_zd():
    sg.Popup('当自动回复开始时请勿关闭任何窗口!!!\nDo not close any windows when automatic reply starts!!!')
    layout3 = [
        [sg.B('中文', font=('黑体', 20)), sg.T('      '), sg.B('English', font=('黑体', 20))],
        [sg.T('要自动回复的联系人:',font=('黑体', 20),key='-1-'), sg.Input()],
        [sg.T('回复的信息:', font=('黑体', 20), key='-2-'), sg.Input()],
        [sg.B('确认', font=('黑体', 15), key='-button1-'), sg.B('返回', font=('黑体', 15), key='-button2-')]
    ]
    window = sg.Window('自动回复', layout3)
    while True:
        event, values = window.read()
        if event == None:
            window.close()
            return 'one'
        if event == '中文':
            window['-1-'].update('要自动回复的联系人:')
            window['-2-'].update('回复的信息:')
            window['-button2-'].update('返回')
            window['-button1-'].update('确认')
        if event == 'English':
            window['-1-'].update('Contacts to be automatically replied to:')
            window['-2-'].update('Reply message:')
            window['-button1-'].update('confirm')
            window['-button2-'].update('return')
        if event == '-button2-':
            window.close()
            return 'one'
        if event == '-button1-':
            sg.Popup('程序开始运行请勿关闭任何窗口')
            print(f'联系人:{values[0]}\n自动回复信息为:{values[1]}')
            listen_list = [str(values[0])]
            zd(listen_list=listen_list,x=values[1])
            return 'stil'


def zd(listen_list,x):
    wx = wxauto.WeChat()

    for i in listen_list:
        wx.AddListenChat(who=i, savepic=True)
    # 持续监听消息，并且收到消息后回复“收到”
    wait = 1  # 设置1秒查看一次是否有新消息
    while True:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            who = chat.who  # 获取聊天窗口名（人或群名）
            one_msgs = msgs.get(chat)  # 获取消息内容
            # 回复收到
            for msg in one_msgs:
                msgtype = msg.type  # 获取消息类型
                content = msg.content  # 获取消息内容，字符串类型的消息内容
                print(f'【{who}】：{content}')
                # ===================================================
                # 处理消息逻辑（如果有）
                #
                # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
                #
                # ===================================================

                # 如果是好友发来的消息（即非系统消息等），则回复收到
                if msgtype == 'friend':
                    chat.SendMsg(x)  # 回复收到
        time.sleep(wait)

def hz_win():
    e = None
    layout = [
        [sg.B('中文', font=('黑体', 20)), sg.T('      '), sg.B('English', font=('黑体', 20))],
        [sg.T('要轰炸的联系人:',font=('黑体', 20),key='-1-'), sg.Input()],
        [sg.T('轰炸信息:', font=('黑体', 20), key='-2-'), sg.Input()],
        [sg.B('确认', font=('黑体', 15), key='-button1-'), sg.B('返回', font=('黑体', 15), key='-button2-')]
    ]
    window = sg.Window('信息轰炸', layout)
    while True:
        event, values = window.read()
        if event == None:
            window.close()
            return 'exit'
        if event == '中文':
            window['-1-'].update('要轰炸的联系人:')
            window['-2-'].update('轰炸信息:')
            window['-button2-'].update('返回')
            window['-button1-'].update('确认')
        if event == 'English':
            window['-1-'].update('Contact person to bomb:')
            window['-2-'].update('Bombing information:')
            window['-button1-'].update('confirm')
            window['-button2-'].update('return')
        if event == '-button1-':
            sg.Popup('确认运行')
            wx = wxauto.WeChat()
            e = 0
            window.close()
            return e,values[0],values[1]
        if event == '-button2-':
            window.close()
            return 'one',values[0],values[1]
def run():
    sdd,sd = None,None
    start = False
    # window_name()
    data = 'one'
    one = None
    while True:
        while True:
            if data == 'one':
                data = init_window0()
            if data == 'two':
                data,one = init_window1()
            if data == 'exit':
                quit(0)
            if data == 'stil':
                pass
            if data == 'set':
                print(one)
                ki = '1'
                break
            if data == 'four':
                data,sd,sdd = hz_win()
            if data == 'three':
                data = win_zd
            if data == 0:
                wx = wxauto.WeChat()
                while True:
                    wx.SendMsg(msg=sdd, who=sd)
        if ki == '1':
            info = window_name(one)
            if info == 'exit':
                data = 'two'
            else:
                start = True
                break
    if start == True:
        sg.Popup('完成程序',font=('宋体',30))
        quit(0)
if __name__ == '__main__':
    sg.Popup('程序开始之前请确保微信已经打开\nPlease ensure that WeChat is open before starting the program')
    run()