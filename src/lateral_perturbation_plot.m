clear
clc

%-------------------------------------------------------------------------
%Loading, Parsing, and Truncating
%-------------------------------------------------------------------------
    perturbation_input = importdata('Lateral_Perturbation.txt');
    perturbation_output = importdata('mocap-006.txt');
    frame=1:1:length(perturbation_input);            
    time_input=(frame-1)*0.0033;                    
    signal_input = perturbation_input(:,2);
    time_output = perturbation_output.data(33090:57336,1);
    time_output = time_output - time_output(1,1);
    signal_output = perturbation_output.data(33090:57336,3);
    signal_output = signal_output - signal_output(1,1);
    signal_output = interp1(time_output,signal_output,time_input);
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
    %Plot
        plot(time_input, signal_input,'Color',[0.815 0.3294 0.3020])
        hold on
        plot(time_input,signal_output,'Color',[0.2157 0.4706 0.7490])
        xlabel('Time (s)')
        ylabel('Lateral Position (m)')
        title('Lateral Perturbation Signal')
        legend('Commanded','Measured')
        xlim([100 200])
    %Saving
        h=figure(1);
        saveas(h,'lateral_perturbation.pdf');
