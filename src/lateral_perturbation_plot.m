% This script generates a plot of the lateral deviation of the treadmill
% base during trial number 6.

%-------------------------------------------------------------------------
% File Paths
%-------------------------------------------------------------------------

PATHS = get_config();

mocap_file = [PATHS.raw_data_dir filesep 'T006' filesep 'mocap-006.txt'];

%-------------------------------------------------------------------------
% Loading, Parsing, and Truncating
%-------------------------------------------------------------------------

start = 33090;
stop = 57336;

perturbation_output = importdata(mocap_file);

time_output = perturbation_output.data(start:stop, 1);
time_output = time_output - time_output(1, 1);

signal_output = perturbation_output.data(start:stop, 3);
signal_output = signal_output - signal_output(1, 1);

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

plot(time_output, signal_output, 'Color', [0.2157 0.4706 0.7490])

box on

xlim([100 200])

xlabel('Time (s)')
ylabel('Lateral Deviation (m)')
title('Lateral Perturbation Signal')

saveas(h, [PATHS.figures_dir filesep 'lateral_perturbation.pdf']);
