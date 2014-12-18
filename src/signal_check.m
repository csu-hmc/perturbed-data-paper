clear
clc

%-------------------------------------------------------------------------
%Loading Files
%-------------------------------------------------------------------------
    input_signals=load('Longitudinal_Perturbation_2.4.2014.txt');
    output_slow=load('record-079_0001.txt');
    output_normal=load('record-080_0001.txt');
    output_fast=load('record-081_0001.txt');
%-------------------------------------------------------------------------
%Declaring Variables
%-------------------------------------------------------------------------
    %Time Variables (necessary because Record Module has varying timestamp)
        time_input=input_signals(:,1);
        output_slow_time=output_slow(:,1); 
        output_slow_time=output_slow_time-output_slow_time(1,1);
        output_normal_time=output_normal(:,1);
        output_normal_time=output_normal_time-output_normal_time(1,1);
        output_fast_time=output_fast(:,1);
        output_fast_time=output_fast_time-output_fast_time(1,1);
    %Speed
        inputs=[input_signals(:,2) input_signals(:,3) input_signals(:,4)];
        output_slow=output_slow(:,2); 
        output_normal=output_normal(:,2);
        output_fast=output_fast(:,2);
%-------------------------------------------------------------------------
%Plotting
%-------------------------------------------------------------------------
    figure(1)
        subplot(3,1,1)
        plot(time_input, inputs(:,1),'Color',[0.815 0.3294 0.3020])
        hold on
        plot(output_slow_time, output_slow,'Color',[0.2157 0.4706 0.7490])
        legend('Commanded','Measured')
        xlim([305 310]); 
        ylabel('Speed (m/s)')
        title('Slow Walking (0.8 m/s)')
    
        subplot(3,1,2)
        plot(time_input, inputs(:,2),'Color',[0.815 0.3294 0.3020])
        hold on
        plot(output_normal_time, output_normal,'Color',[0.2157 0.4706 0.7490])
        ylabel('Speed (m/s)')
        xlim([305 310]); 
        title('Normal Walking (1.2 m/s)')
    
        subplot(3,1,3)
        plot(time_input,inputs(:,3),'Color',[0.815 0.3294 0.3020])
        hold on
        plot(output_fast_time,output_fast,'Color',[0.2157 0.4706 0.7490])
        ylabel('Speed (m/s)')
        xlim([305 310]); xlabel('Time (s)')
        title('Fast Walking (1.6 m/s)')
        
        h=figure(1);
        saveas(h,'input_vs_output.pdf')
