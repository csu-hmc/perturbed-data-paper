function paths = get_config()

    script_path = mfilename('fullpath');
    root_dir_path = fileparts(fileparts(script_path));

    user_config = [root_dir_path filesep 'config.yml'];

    if exist(user_config, 'file') == 2
        yaml_file = user_config;
    else
        yaml_file = [root_dir_path filesep 'default-config.yml'];
    end

    paths = parse_yaml(yaml_file, root_dir_path);

end


function paths = parse_yaml(path, root_dir_path)

    fid = fopen(path);

    tline = fgets(fid);
    while ischar(tline)
        parts = strsplit(tline, ': ');
        name = parts{1};
        path = parts{2};
        if path(1) == '\' || path(2) == ':'
            % is an absolute path on unix or windows
            paths.(name) = path;
        else
            paths.(name) = [root_dir_path filesep path];
        end
        tline = fgets(fid);
    end

    fclose(fid);

end
