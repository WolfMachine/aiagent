# get_files_info.py

import os

def get_files_info(working_directory, directory="."):
    if not isinstance(working_directory, str) or not working_directory:
        return "Error: working directory must be a non-empty string!"
    if not isinstance(directory, str) or not directory:
        return "Error: directory must be a non-empty string!"
    joined_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(joined_path)
    working_dir_abs = os.path.abspath(working_directory)
    try:
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except ValueError:
        # Paths are on different drives (Windows)
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    file_list = os.listdir(full_path)

    file_list_info = ""

    for file in file_list:
        file_path = os.path.join(full_path, file)
        file_size = os.path.getsize(file_path)
        file_is_directory = os.path.isdir(file_path)
        file_list_info += f"- {file}: file_size={file_size} bytes, is_dir={file_is_directory}\n"
    return file_list_info



