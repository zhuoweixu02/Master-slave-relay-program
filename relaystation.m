function [data_table] = relaystation(master_serial,slave_serial)

voltage_from_sensor=0;
table = zeros(2000,2000);
times_of_while=0;
times_of_loop=0;
latest_fprintf=0;
%figure;
%pause(1);
tic;
while true
    times_of_while=times_of_while+1;
    if latest_fprintf>30
        break;
    end
    %if strcmpi(get(gcf,'CurrentCharacter'),'e')
    %    break;
    %end
    if toc-latest_fprintf<0.04
        continue
    else
        latest_fprintf=toc;
        %target=inputfunction(latest_fprintf);%去编一个输入生成函数
        target=1.23;
        target_str=num2str(target);
        target_str=[target_str,'00.00'];
        position_of_dot=find(target_str=='.');
        target_str=target_str(1:position_of_dot+2);%把target的数位控制在两位
         if target_str(1)~='-'
            target_str=['+',target_str];
        end
    end
    times_of_loop=times_of_loop+1;
    fprintf(slave_serial,'#');%向slave写入触发串口回调函数
    voltage_from_sensor=fscanf(slave_serial,'%g')
    if ~isempty(voltage_from_sensor)
        table(times_of_loop,5)=voltage_from_sensor;
    end
    data=num2str(voltage_from_sensor);%float转ch
    fprintf(master_serial,target);%向上位机写入数据  -10.00*+5.22*
    table(times_of_loop,1)=times_of_while;%列1记录循环次数
    table(times_of_loop,2)=target;
    table(times_of_loop,3)=latest_fprintf;
    voltage_from_master=fscanf(master_serial,'%g');
    if ~isempty(voltage_from_master)
        table(times_of_loop,4)=voltage_from_master;
    end
    data_table=table;
end