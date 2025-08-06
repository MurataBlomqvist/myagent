import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from const import MAX_LOOP_COUNT

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info
        , schema_get_file_content
        , schema_run_python_file
        , schema_write_file
    ]
)

def exception_handler(exception_text):
    # reducing boilerplate code in 2025 is the new vibe(coding)
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

def generate_response(model_name, api_key, verbose_flag, system_prompt, messages):
    client = genai.Client(api_key=api_key)

    for i in range(0, MAX_LOOP_COUNT):

        response = client.models.generate_content(
            model=model_name
            , contents=messages
            , config=types.GenerateContentConfig(
                tools=[available_functions]
                , system_instruction=system_prompt
                )
        )

        for candidate in  response.candidates:
            messages.append(candidate.content)
        
        if not response.function_calls is None:
            for functionSpec in response.function_calls:
                #print(functionSpec)
                func_args = ""
                if (not functionSpec.args is None):
                    func_args = functionSpec.args

                called_function_result = call_function(functionSpec, verbose_flag)
                if called_function_result.parts[0].function_response.response is None:
                    raise Exception("Error no response from function")

                elif (
                    not called_function_result.parts[0].function_response.response is None
                    and verbose_flag
                ):
                    print(f"-> {called_function_result.parts[0].function_response.response}")

                messages.append(
                    called_function_result
                )

        else:
            print(f"\n{response.text}")
            return response

    

def main():
    # initialize flags for printing output
    verbose_flag = False
    # init the env variables
    model_name, api_key = load_env_variables()

    system_prompt = ""
    #init system prompt
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory and you do not need to specify the working directory in your function calls as it is automatically injected for security reasons when you call the function.
        Start each function call plan with listing the working directory and reading the content of the files that the user_prompt might want.

    """

    print("Starting myagent!")
    if len(sys.argv) < 2:
        print("user prompt is not provided")
        print('uv run main.py "[type your prompt here]"')
        return
    user_prompt = sys.argv[1]

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = generate_response(model_name, api_key, verbose_flag, system_prompt, messages)

    if verbose_flag:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
