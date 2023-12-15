import serial
class Datafromslave:
    def __init__(self, data, availability):
        self.data = data
        self.availability = availability

def getdata(x):
    datastr = x.readline()  # 获取arduino发送的数据
    datastring = datastr.decode("utf-8")
    flag = True #默认是有响应数据的

    if len(str) < 3:
        print("no response")
        flag = False
    else:
        if datastring[:1] != '-':
            datastring = "+" + datastring

    n = datastring.find('\n')  # 确定斜杠的位置
    datastring = datastring[:n]  # 读取斜杠前的数据
    data = Datafromslave(datastring, flag)
    return data