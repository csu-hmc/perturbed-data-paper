function data = parse_record(path)
% function data = parse_record(path)
%
% Parses a record-xxx.txt file the slow way and returns the numerical data
% sans the events.

file = fopen(path);

lines = textscan(file, '%s', 'Delimiter', '\n', 'CommentStyle', '#');
lines = lines{:};

data = zeros(length(lines) - 1, 4);

for i = 2:length(lines)
    data(i - 1, :) = str2num(lines{i, :});
end

fclose(file);
