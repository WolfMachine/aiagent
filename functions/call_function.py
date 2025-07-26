# call_function.py
from google.genai import types
import config

WORKING_DIRECTORY = "./calculator"

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

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

    # If the function name is in our dictionary of functions
    if function_call_part.name in functions:

        # Call the function and "capture" the result
        function_result =  functions[function_call_part.name](WORKING_DIRECTORY,
                                                              **function_call_part.args)
        return types.Content( #return the function_result
                            role="tool",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call_part.name,
                                    response={"result": function_result},
                                )
                            ],
                        )

    # If the function could not be called
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

