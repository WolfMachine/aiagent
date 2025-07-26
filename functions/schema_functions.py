# functions.schema_functions.py

from google import genai


# get_files_info
schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# get_file_content
schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a file, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path to the file to read from, relative to the working directory. If not provided, reads file in the working directory itself.",
            ),
        },
    ),
)

# run_python_file
schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to the python file to run, relative to the working directory. If not provided, runs the python file in the working directory itself.",
            ),
        },
    ),
)

# write_file
schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Write a file, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to write the file to, relative to the working directory. If not provided, writes the file into the working directory itself.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)
available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)


