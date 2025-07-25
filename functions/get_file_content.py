# get_file_content.py

import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    if not isinstance(working_directory, str) or not working_directory:
        return "Error: working directory must be a non-empty string!"
    if not isinstance(file_path, str) or not file_path:
        return "Error: file path must be a non-empty string!"
    joined_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(joined_path)
    working_dir_abs = os.path.abspath(working_directory)    
    try:
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except ValueError:
        # Paths are on different drives (Windows)
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    file_content_string = None
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            file_content_string = f.read(MAX_CHARS)
            current_position = f.tell()  # Get current file pointer position
        
        # Check if file was truncated
        file_stat = os.stat(full_path)
        if current_position < file_stat.st_size:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except PermissionError:
        return 'Error: Permissions denied access to the file.'
    except Exception as e:
        return f'Error: An exception has occured: {e}'

    if not file_content_string:
        file_content_string = "Error: File was not read."

    return file_content_string
