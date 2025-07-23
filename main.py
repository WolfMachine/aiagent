# main.py
import sys
import os
import flags
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

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
    model='gemini-2.0-flash-001', contents=messages
    )
    print("Gemini Response:")
    print(response.text)  
    print_tokens(response.usage_metadata.prompt_token_count,response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
