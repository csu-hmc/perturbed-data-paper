clear
clc

%-------------------------------------------------------------------------
%Loading Files
%-------------------------------------------------------------------------
    input_signals = importdata('Longitudinal_Perturbation_2.4.2014.txt');
    output_slow = importdata('record-076.txt');
    output_normal = importdata('record-077.txt');
    output_fast = importdata('record-078.txt');
%-------------------------------------------------------------------------
%Declaring Variables
%-------------------------------------------------------------------------
    %Time Variables (necessary because Record Module has varying timestamp)
        time_input = input_signals(:,1);
        output_slow_time = output_slow.data(:,1); 
        output_slow_time = output_slow_time-output_slow_time(1,1);
        output_normal_time = output_normal.data(:,1);
        output_normal_time = output_normal_time-output_normal_time(1,1);
        output_fast_time = output_fast.data(:,1);
        output_fast_time  =output_fast_time-output_fast_time(1,1);
    %Speed
        inputs=[input_signals(:,2) input_signals(:,3) input_signals(:,4)];
        output_slow = output_slow.data(:,2); 
        output_normal = output_normal.data(:,2);
        output_fast = output_fast.data(:,2);
%-------------------------------------------------------------------------
%Plotting
%-------------------------------------------------------------------------
    %Settings to Improve Graph Appearance
        ti = get(gca,'TightInset');
        set(gca,'Position',[ti(1) ti(2) 1-ti(3)-ti(1) 1-ti(4)-ti(2)]);
        set(gca,'units','centimeters')
        pos = get(gca,'Position');
        ti = get(gca,'TightInset');
        set(gcf, 'PaperUnits','centimeters');
        set(gcf, 'PaperSize', [pos(3)+ti(1)+ti(3) pos(4)+ti(2)+ti(4)]);
        set(gcf, 'PaperPositionMode', 'manual');
        set(gcf, 'PaperPosition',[0 0 pos(3)+ti(1)+ti(3) pos(4)+ti(2)+ti(4)]);
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
