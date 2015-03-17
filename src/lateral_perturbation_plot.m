% This script generates a plot of the lateral deviation of the treadmill
% base durig trial number 6.

clear
clc

%-------------------------------------------------------------------------
% File Paths
%-------------------------------------------------------------------------

PATHS = get_config();

per_sig_dir = [PATHS.raw_data_dir filesep 'perturbation-signals'];
lat_per_file = [per_sig_dir filesep 'lateral-perturbation.txt'];
mocap_file = [PATHS.raw_data_dir filesep 'T006' filesep 'mocap-006.txt'];

%-------------------------------------------------------------------------
% Loading, Parsing, and Truncating
%-------------------------------------------------------------------------

perturbation_input = importdata(lat_per_file);
frame = 1:1:length(perturbation_input);
time_input = (frame - 1) * 0.0033;
signal_input = perturbation_input(:, 2);

perturbation_output = importdata(mocap_file);
time_output = perturbation_output.data(33090:57336, 1);
time_output = time_output - time_output(1, 1);
signal_output = perturbation_output.data(33090:57336, 3);
signal_output = signal_output - signal_output(1, 1);
signal_output = interp1(time_output,signal_output,time_input);

%-------------------------------------------------------------------------
% Plotting
%-------------------------------------------------------------------------

h = figure();

fig_width = 5.0;
golden_ratio = (1 + sqrt(5)) / 2;
fig_height = fig_width / golden_ratio;

set(gcf, ...
    'Color', [1, 1, 1], ...
    'PaperOrientation', 'portrait', ...
    'PaperUnits', 'inches', ...
    'PaperPositionMode', 'manual', ...
    'OuterPosition', [424, 305 - 50, 518, 465], ...
    'PaperPosition', [0, 0, fig_width, fig_height], ...
    'PaperSize', [fig_width, fig_height])

hold on

plot(time_input, signal_input, 'Color', [0.815 0.3294 0.3020])
plot(time_input, signal_output, 'Color', [0.2157 0.4706 0.7490])

xlim([100 200])

xlabel('Time (s)')
ylabel('Lateral Position (m)')
title('Lateral Perturbation Signal')
legend('Commanded', 'Measured')

saveas(h, [PATHS.figures_dir filesep 'lateral_perturbation.pdf']);
