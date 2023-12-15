%11.14
%加入了正弦函数生成的代码，能够成功与上下位机通讯
%利用arduino端的serial event函数实现通讯，频率约为25赫兹
%删去了循环开始前的serial event触发，提高时效性
close all;
clear all;
clc;%matlab的‘初始化’
delete(instrfind({'Port'},{'COM3'}));
delete(instrfind({'Port'},{'COM4'}));
delete(instrfind({'Port'},{'COM5'}));
delete(instrfind({'Port'},{'COM6'}));
delete(instrfind({'Port'},{'COM7'}));%关闭串口；
master_serial = serial('COM3');%气阀控制mega是6
master_serial.BaudRate = 115200;
slave_serial = serial('COM4');%实验室采集板是4
slave_serial.BaudRate = 115200;%命名串口并设置波特率
fopen(master_serial);
fopen(slave_serial);%打开串口
data_table = relaystation(master_serial,slave_serial);