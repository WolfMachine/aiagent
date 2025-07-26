# run_python.py

import os
from subprocess import run


def run_python_file(working_directory, file_path, args=None):
    if not args:
        args = []
    if not isinstance(working_directory, str) or not working_directory:
        return "Error: working directory must be a non-empty string!"
    if not isinstance(file_path, str) or not file_path:
        return "Error: file path must be a non-empty string!"
    joined_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(joined_path)
    working_dir_abs = os.path.abspath(working_directory)
    try:
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except ValueError:
        # Paths are on different drives (Windows)
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = run(["python", full_path] + args,
                                capture_output=True,
                                timeout=30,
                                cwd=working_dir_abs
                                )
    except Exception as e:
        return f'Error: executing Python file: {e}'


    output = ''
    return_code_output = ''

    
    if completed_process.returncode:
            return_code_output += f'Process exited with code {completed_process.returncode}\n'

    if completed_process.stderr:        
        output += "STDERR:\n" + completed_process.stderr.decode() + '\n'
    if completed_process.stdout:
        output += "STDOUT:\n" + completed_process.stdout.decode()
    if output or return_code_output:
        return output + return_code_output

    return 'No output Produced.'

