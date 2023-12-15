# -*- coding: utf-8 -*-
# 10.9
# 通过continue来规避无响应请求
# 已封装
import time
import serial
import keyboard
import queue
import keyboard_monitor
import relaystation



test = b"3"
print("b3=")
print(test)
print("\n")

serialPort_slave = "COM5"  # 获取采集板数据的下位机串口
serialPort_master = "COM4"  # 操控气阀的主机串口
baudRate = 115200  # 波特率
ser_slave = serial.Serial(serialPort_slave, baudRate, timeout=0.1)
ser_master = serial.Serial(serialPort_master, baudRate, timeout=0.1)
print("参数设置：串口=%s ，波特率=%d" % (serialPort_slave, baudRate))
print("参数设置：串口=%s ，波特率=%d" % (serialPort_master, baudRate))

station = relaystation.Relaystation(ser_slave, ser_master)





