# main.py
import sys
import os
import flags
from dotenv import load_dotenv
import functions.schema_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def print_token_count(prompt_token_count, candidates_token_count):
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}")

def print_user_prompt(prompt): 
    print(f"User prompt: {prompt}\n")

def noop(*args, **kwargs):
    pass

def main():
    active_flags = set()
    if len(sys.argv) < 2:
        print("Enter a prompt first!\nExample: main.py Why did the chicken cross the road?")
        sys.exit(1) 
    else:
        plain_args = []
        for arg in sys.argv[1:]:
            if arg.startswith('-'):
                # normalize the flag
                flag_arg = flags.normalize_flag(arg)
                # add valid flag to flag list
                active_flag = flags.flag_map.get(flag_arg)
                if active_flag:
                    active_flags.add(active_flag)
                continue
            plain_args.append(arg)
        # print(f"Type: {sys.argv}\nLength: {len(sys.argv)}\nContents: {sys.argv}")
        user_prompt = ' '.join(plain_args)


    print_tokens = print_token_count if flags.Flags.VERBOSE in active_flags else noop
    print_prompt = print_user_prompt if flags.Flags.VERBOSE in active_flags else noop

    print_prompt(user_prompt)
    messages = [
            genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=genai.types.GenerateContentConfig(
                tools=[functions.schema_functions.available_functions],
                system_instruction=system_prompt
                ),
    )
    print("Gemini Response:")
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    if response.text:
        print(response.text)  
    print_tokens(response.usage_metadata.prompt_token_count,response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
