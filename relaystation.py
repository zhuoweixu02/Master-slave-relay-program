import time
import serial
import keyboard
import queue

class Datafromslave:
    def __init__(self, data, availability):
        self.data = data
        self.availability = availability

def getdata(x):
    datastr = x.readline()  # 获取arduino发送的数据
    datastring = datastr.decode("utf-8")
    flag = True #默认是有响应数据的

    if len(datastring) < 3:
        print("no response")
        flag = False
    else:
        if datastring[:1] != '-':
            datastring = "+" + datastring

    n = datastring.find('\n')  # 确定斜杠的位置
    datastring = datastring[:n]  # 读取斜杠前的数据
    data = Datafromslave(datastring, flag)
    return data

class Relaystation():
    def __init__(self, ser_slave, ser_master):
        q = queue.Queue(8)

        flag = False

        def targetimport(x):
            global flag
            a = keyboard.KeyboardEvent(event_type='down', scan_code=2, name='1')
            b = keyboard.KeyboardEvent(event_type='down', scan_code=3, name='2')
            c = keyboard.KeyboardEvent(event_type='down', scan_code=4, name='3')
            d = keyboard.KeyboardEvent(event_type='down', scan_code=5, name='4')
            e = keyboard.KeyboardEvent(event_type='down', scan_code=6, name='5')
            f = keyboard.KeyboardEvent(event_type='down', scan_code=7, name='6')
            g = keyboard.KeyboardEvent(event_type='down', scan_code=8, name='7')
            h = keyboard.KeyboardEvent(event_type='down', scan_code=9, name='8')
            i = keyboard.KeyboardEvent(event_type='down', scan_code=10, name='9')
            j = keyboard.KeyboardEvent(event_type='down', scan_code=11, name='0')
            k = keyboard.KeyboardEvent(event_type='down', scan_code=41, name='dot')
            l = keyboard.KeyboardEvent(event_type='down', scan_code=28, name='enter')
            m = keyboard.KeyboardEvent(event_type='down', scan_code=14, name='backspace')

            if x.event_type == a.event_type and ( x.scan_code == a.scan_code or x.scan_code == b.scan_code or x.scan_code == c.scan_code or x.scan_code == d.scan_code or x.scan_code == e.scan_code or x.scan_code == f.scan_code or x.scan_code == g.scan_code or x.scan_code == h.scan_code or x.scan_code == i.scan_code or x.scan_code == j.scan_code):
                tmp = (x.scan_code - 1) % 10
                q.put(tmp)
                # print(tmp)
            else:
                if x.event_type == l.event_type and x.scan_code == l.scan_code:
                    # print(x.scan_code)
                    if q.qsize() < 3:
                        print("非法的输入，请撤销")
                    else:
                        flag = True
                else:
                    if x.event_type == m.event_type and x.scan_code == m.scan_code:
                        q.queue.clear()
                        print("成功撤销上一次键入")

        # 将0转换为ASCII码方便发送
        demo2 = b"8"  # 同理

        keyboard.hook(targetimport)  # 埋下的钩子，随键盘输入触发，与控制程序并行
        angle = 0
        while 1:
            voltage = getdata(ser_slave)
            if not voltage.availability:
                continue

            if flag:
                print("you press enter")
                target = 0
                num_iter = 3  # 输入值为三位数
                for j in range(num_iter):
                    target = target * 10 + q.get()
                print(target)
                angle = target
                q.queue.clear()
                flag = False
            if angle < 100:
                if angle < 10:
                    anglechar = "00" + '%d' % angle
                else:
                    anglechar = "0" + '%d' % angle
            else:
                anglechar = '%d' % angle

            voltage3 = voltage.data
            voltage3 = voltage3 + anglechar

            message1 = voltage3.encode("utf-8")
            ser_master.write(message1)  # 转换数据格式并发送
            str = ser_master.readline()
            print("发送的数据为")
            print(voltage3)
            print("单片机读取到的目标为")
            print(str)

            #print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())));
            print("\n")

        self.__voltage1 = angle
        self.__target = angle

    def getVoltage(self):
        return self.__voltage1
    def getTarget(self):
        return self.__target
