# write_file.py

import os

def write_file(working_directory, file_path, content):
    if not isinstance(working_directory, str) or not working_directory:
        return "Error: working directory must be a non-empty string!"
    if not isinstance(file_path, str) or not file_path:
        return "Error: file path must be a non-empty string!"
    joined_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(joined_path)
    working_dir_abs = os.path.abspath(working_directory)
    try:
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except ValueError:
        # Paths are on different drives (Windows)
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Exception {e} when trying to open {file_path} for writing.'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

