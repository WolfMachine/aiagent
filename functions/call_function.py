# call_function.py

import config

from get_files_info import get_files_info
from get_file_content import get_file_content
from write_file import write_file
from run_python import run_python_file

functions = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "write_file" : write_file,
        "run_python_file" : run_python_file
}

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    functions[function_call_part.name](WORKING_DIRECTORY, function_call_part.args)
