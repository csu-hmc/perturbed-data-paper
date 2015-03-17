%-------------------------------------------------------------------------
% File Paths
%-------------------------------------------------------------------------

PATHS = get_config();

raw_dir = PATHS.raw_data_dir;

per_sig_dir = [raw_dir filesep 'perturbation-signals'];
commanded_file = [per_sig_dir filesep 'longitudinal-perturbation.txt'];

measured_076 = [raw_dir filesep 'T076' filesep 'record-076.txt'];
measured_077 = [raw_dir filesep 'T077' filesep 'record-077.txt'];
measured_078 = [raw_dir filesep 'T078' filesep 'record-078.txt'];

%-------------------------------------------------------------------------
% Loading Files
%-------------------------------------------------------------------------

input_signals = importdata(commanded_file);
output_slow = parse_record(measured_076);
output_normal = parse_record(measured_077);
output_fast = parse_record(measured_078);

%-------------------------------------------------------------------------
% Declaring Variables
%-------------------------------------------------------------------------

% Time Variables (necessary because Record Module has varying timestamp)
time_input = input_signals.data(:, 1);

output_slow_time = output_slow(:, 1);
output_slow_time = output_slow_time - output_slow_time(1, 1);

output_normal_time = output_normal(:, 1);
output_normal_time = output_normal_time - output_normal_time(1, 1);

output_fast_time = output_fast(:, 1);
output_fast_time  = output_fast_time - output_fast_time(1, 1);

% Speed
inputs = [input_signals.data(:, 2) input_signals.data(:, 3) ...
          input_signals.data(:, 4)];
output_slow = output_slow(:, 2);
output_normal = output_normal(:, 2);
output_fast = output_fast(:, 2);

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

red = [0.815 0.3294 0.3020];
blue = [0.2157 0.4706 0.7490];


% Slow
subplot(3, 1, 1)
hold on

plot(time_input, inputs(:, 1), 'Color', red)
plot(output_slow_time, output_slow, 'Color', blue)
xlim([305 310]);

box on

leg = legend('Commanded', 'Measured');
set(leg,'FontSize', 6);

ylabel('Speed (m/s)')
title('Slow Walking (0.8 m/s)')

% Normal
subplot(3, 1, 2)
hold on

plot(time_input, inputs(:, 2), 'Color', red)
plot(output_normal_time, output_normal, 'Color', blue)
xlim([305 310]);

box on

ylabel('Speed (m/s)')
title('Normal Walking (1.2 m/s)')

% Fast
subplot(3, 1, 3)
hold on

plot(time_input, inputs(:, 3), 'Color', red)
plot(output_fast_time, output_fast, 'Color', blue)
xlim([305 310])

box on

xlabel('Time (s)')
ylabel('Speed (m/s)')
title('Fast Walking (1.6 m/s)')

saveas(h, [PATHS.figures_dir filesep 'input_vs_output.pdf'])
