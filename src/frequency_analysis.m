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

% Create new input time to eliminate repeated values from original file
time_input = 0:0.0033:round(input_signals.data(end, 1));
new_time = 0:0.01:round(time_input(end));
output_slow_time = output_slow(:, 1) - output_slow(1, 1);
output_normal_time = output_normal(:, 1) - output_normal(1, 1);
output_fast_time = output_fast(:, 1) - output_fast(1, 1);
inputs = input_signals.data(:, 2:4);

%-------------------------------------------------------------------------
% Interpolate Data
%-------------------------------------------------------------------------

inputs = interp1(time_input, inputs, new_time);
outputs = [interp1(output_slow_time, output_slow(:, 2), new_time'), ...
           interp1(output_normal_time, output_normal(:, 2), new_time'), ...
           interp1(output_fast_time, output_fast(:, 2), new_time')];
outputs(isnan(outputs)) = 0;

% Clip for Longitudinal Perturbations only
inputs = inputs(9000:57000, :);
outputs = outputs(9000:57000, :);

%-------------------------------------------------------------------------
%Spectral Analysis
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

% Analysis
fs = 100;
T = 1 / fs;
nfft = 2000;
w = nfft;
noverlap = nfft / 2;
speeds  =  size(outputs, 2);

for i=1:speeds

    % Remove Spike at 0 Hz
    x_input = inputs(:, i) - mean(inputs(:, i));
    x_output = outputs(:, i) - mean(outputs(:, i));

    % Spectrograms
    [s_input, f_input, tpsd_input, p_input] = spectrogram(x_input, w, noverlap, nfft, fs);
    [s_output, f_output, tpsd_output, p_output] = spectrogram(x_output, w, noverlap, nfft, fs);

    % Spectral Averaging
    p_input_mean = mean(p_input, 2);
    p_output_mean = mean(p_output, 2);

    % Plotting
    titles={'Slow Walking (0.8 ms^{-1})', 'Normal Walking (1.2 ms^{-1})', 'Fast Walking (1.6 ms^{-1})'};
    subplot(speeds, 1, i)
    semilogy(f_input, p_input_mean, 'Color', red)
    hold on
    semilogy(f_output, p_output_mean, 'Color', blue)

    xlim([0 8]); ylim([10^-5 10^0])

    set(gca, 'FontSize', 6)  % sets axis tick font size
    ylabel('PSD [m^2 s^{-2} Hz^{-1}]', 'FontSize', 6)
    title(titles{i}, 'FontSize', 8)

    if i==1
        leg = legend('Commanded', 'Measured', 'Location', 'northeast');
        set(leg,'FontSize', 6);
    end

    if i==3
        xlabel('Frequency [Hz]', 'FontSize', 8);
    end

end

saveas(h, [PATHS.figures_dir filesep 'frequency_analysis.pdf'])
