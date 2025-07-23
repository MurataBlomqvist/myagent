import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def exception_handler(exception_text):
    # reducing boilerplate code in 2025 is the new vibe
    raise Exception(exception_text)

def load_env_variables():
    load_dotenv()
    model_name = os.environ.get("GEMINI_MODEL_NAME")
    api_key = os.environ.get("GEMINI_API_KEY")

    if (api_key is None):
        exception_handler("api key could not be read from .env file")
    if (model_name is None):
        exception_handler("model name could not be read from .env file")
    
    return model_name, api_key

def generate_response(model_name, api_key, verbose_flag, messages):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model_name
        , contents=messages
    )

    print(response.text)
    if verbose_flag:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    # initialize flags for printing output
    verbose_flag = False
    # init the env variables
    model_name, api_key = load_env_variables()

    print("Starting myagent!")
    if len(sys.argv) < 2:
        #raise Exception("User prompt not provided")
        print("user prompt is not provided")
        print('uv run main.py "[type your prompt here]"')
        return
    user_prompt = sys.argv[1]

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_response(model_name, api_key, verbose_flag, messages)

if __name__ == "__main__":
    main()
