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

% Settings to Improve Graph Appearance

% TODO : I have no idea what this does and the figure doesn't come out to
% an adequate size. I think it may just crop the image from the default
% size which is incorrect.

ti = get(gca, 'TightInset');
set(gca, 'Position', [ti(1) ti(2) 1-ti(3)-ti(1) 1-ti(4)-ti(2)]);
set(gca, 'units', 'centimeters')
pos = get(gca, 'Position');
ti = get(gca, 'TightInset');
set(gcf, 'PaperUnits', 'centimeters');
set(gcf, 'PaperSize',  [pos(3)+ti(1)+ti(3) pos(4)+ti(2)+ti(4)]);
set(gcf, 'PaperPositionMode',  'manual');
set(gcf, 'PaperPosition', [0 0 pos(3)+ti(1)+ti(3) pos(4)+ti(2)+ti(4)]);

% Plot

hold on

plot(time_input, signal_input, 'Color', [0.815 0.3294 0.3020])
plot(time_input, signal_output, 'Color', [0.2157 0.4706 0.7490])

xlim([100 200])

xlabel('Time (s)')
ylabel('Lateral Position (m)')
title('Lateral Perturbation Signal')
legend('Commanded', 'Measured')

% Saving

h = figure(1);
saveas(h, [PATHS.figures_dir filesep 'lateral_perturbation.pdf']);
