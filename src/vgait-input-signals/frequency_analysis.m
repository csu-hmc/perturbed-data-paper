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
%Spectral Analysis
%-------------------------------------------------------------------------
    Fs=100;
    T=1/Fs;
    %Lengths
        L_inputs = length(inputs);
        L_output_slow=length(output_slow);
        L_output_normal = length(output_normal);
        L_output_fast = length(output_fast);
    %NFFT
        NFFT_inputs=2^nextpow2(L_inputs);
        NFFT_output_slow = 2^nextpow2(L_output_slow);
        NFFT_output_normal = 2^nextpow2(L_output_normal);
        NFFT_output_fast = 2^nextpow2(L_output_fast);
    %FI
        fi_inputs = Fs/2*linspace(0,1,NFFT_inputs/2+1);
        fi_output_slow=Fs/2*linspace(0,1,NFFT_output_slow/2+1);
        fi_output_normal=Fs/2*linspace(0,1,NFFT_output_normal/2+1);
        fi_output_fast=Fs/2*linspace(0,1,NFFT_output_fast/2+1);
    %Y
        Y_input = fft(inputs,NFFT_inputs)/L_inputs;
        Y_output_slow = fft(output_slow,NFFT_output_slow)/L_output_slow;
        Y_output_normal = fft(output_normal,NFFT_output_normal)/L_output_normal;
        Y_output_fast = fft(output_fast,NFFT_output_fast)/L_output_fast;
        
%-------------------------------------------------------------------------
%Plotting
%-------------------------------------------------------------------------
    set(0,'defaulttextinterpreter','latex')
    set(0,'DefaultAxesFontName', 'latex')
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
        plot(fi_inputs,2*abs(Y_input(1:NFFT_inputs/2+1,1)),'k')
        hold on
        plot(fi_output_slow,2*abs(Y_output_slow(1:NFFT_output_slow/2+1)),'r')
        legend('Input','Output')
        title('Slow Walking (0.8 m/s)','Fontweight','bold')
        ylabel('|Y(f)|','Fontweight','bold')
        ylim([0 6*10^-3]); xlim([0 8])
    
        subplot(3,1,2)
        plot(fi_inputs,2*abs(Y_input(1:NFFT_inputs/2+1,2)),'k')
        hold on
        plot(fi_output_normal,2*abs(Y_output_slow(1:NFFT_output_normal/2+1)),'r')
        legend('Input','Output')
        title('Normal Walking (1.2 m/s)','Fontweight','bold')
        ylabel('|Y(f)|','Fontweight','bold')
        ylim([0 0.015]); xlim([0 8])
        
        subplot(3,1,3)
         plot(fi_inputs,2*abs(Y_input(1:NFFT_inputs/2+1,3)),'k')
        hold on
        plot(fi_output_fast,2*abs(Y_output_fast(1:NFFT_output_fast/2+1)),'r')
        legend('Input','Output')
        title('Fast Walking (1.6 m/s)','Fontweight','bold')
        xlabel('Frequency (Hz)','Fontweight','bold')
        ylabel('|Y(f)|','Fontweight','bold')
        ylim([0 0.03]); xlim([0 8])
        
        h=figure(1);
        saveas(h,'frequency_analysis.pdf');
        
        
