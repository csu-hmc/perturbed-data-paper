clear
clc

%-------------------------------------------------------------------------
%Loading Files
%-------------------------------------------------------------------------
    input_signals = importdata('Longitudinal_Perturbation_2.4.2014.txt');
    output_slow_file = fopen('record-076.txt');
    output_normal_file = fopen('record-077.txt');
    output_fast_file = fopen('record-078.txt');
%-------------------------------------------------------------------------
%Parse Events from Files
%-------------------------------------------------------------------------
    %Remove Lines Starting with #
        output_slow_parse = textscan(output_slow_file,'%s', 'Delimiter', '\n', 'CommentStyle', '#');
        output_slow_parse = output_slow_parse{:};
        output_normal_parse = textscan(output_normal_file,'%s', 'Delimiter', '\n', 'CommentStyle', '#');
        output_normal_parse = output_normal_parse{:};
        output_fast_parse = textscan(output_fast_file,'%s', 'Delimiter', '\n', 'CommentStyle', '#');
        output_fast_parse = output_fast_parse{:};
    %Preallocating
        output_slow = zeros(length(output_slow_parse)-1,4);
        output_normal = zeros(length(output_normal_parse)-1,4);
        output_fast = zeros(length(output_fast_parse)-1,4);
    %Recreate Matrices 
        for i = 2:length(output_slow_parse)
            output_slow(i-1,:) = str2num(output_slow_parse{i,:});
        end
        for i = 2:length(output_normal_parse)
            output_normal(i-1,:) = str2num(output_normal_parse{i,:});
        end
        for i = 2:length(output_fast_parse)
            output_fast(i-1,:) = str2num(output_fast_parse{i,:});
        end
%-------------------------------------------------------------------------
%Declaring Variables
%-------------------------------------------------------------------------
    time_input=0:0.0033:round(input_signals(end,1));     %Create new input time to eliminate repeated values from original file
    new_time=0:0.01:round(time_input(end));         
    output_slow_time=output_slow(:,1)-output_slow(1,1); 
    output_normal_time=output_normal(:,1)-output_normal(1,1);
    output_fast_time=output_fast(:,1)-output_fast(1,1);
    inputs=input_signals(:,2:4);
%-------------------------------------------------------------------------
%Interpolate Data
%-------------------------------------------------------------------------
    inputs=interp1(time_input,inputs,new_time);
    outputs=[interp1(output_slow_time,output_slow(:,2),new_time'),...
             interp1(output_normal_time,output_normal(:,2),new_time'),...
             interp1(output_fast_time,output_fast(:,2),new_time')];
    outputs(isnan(outputs))=0;
    %Clip for Longitudinal Perturbations only
        inputs=inputs(9000:57000,:);
        outputs=outputs(9000:57000,:);
%-------------------------------------------------------------------------
%Spectral Analysis
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
    %Analysis
        fs=100;
        T=1/fs;
        nfft=2000;  
        w=nfft;  
        noverlap=nfft/2; 
        speeds = size(outputs,2);
    for i=1:speeds
        %Remove Spike at 0 Hz
            x_input = inputs(:,i) - mean(inputs(:,i));
            x_output = outputs(:,i) - mean(outputs(:,i));  
        %Spectrograms
            [s_input,f_input,tpsd_input,p_input] = spectrogram(x_input,w,noverlap,nfft,fs);
            [s_output,f_output,tpsd_output,p_output] = spectrogram(x_output,w,noverlap,nfft,fs);
        %Spectral Averaging
            p_input_mean = mean(p_input,2);  
            p_output_mean = mean(p_output,2);
        %Plotting
            titles={'Slow Walking (0.8 m/s)','Normal Walking (1.2 m/s)','Fast Walking (1.6 m/s)'};
            figure(1)
                subplot(speeds,1,i)
                semilogy(f_input,p_input_mean,'Color',[0.815 0.3294 0.3020])
                hold on
                semilogy(f_output,p_output_mean,'Color',[0.2157 0.4706 0.7490])
                ylabel('PSD (m^2s^{-2}/Hz)')
                xlim([0 8]); ylim([10^-5 10^0])
                title(titles{i})
                if i==1
                    legend('Commanded','Measured','Location','northeast')
                end
                if i==3
                    xlabel('Frequency (Hz)');
                end
    end
        h=figure(1);
        saveas(h,'frequency_analysis.pdf');