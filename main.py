import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

model_name = "gemini-2.0-flash-001"

def main():
    # initialize flags for printing output
    verbose_flag = False

    print("Starting myagent!")
    if len(sys.argv) < 2:
        raise Exception("User prompt not provided")
    user_prompt = sys.argv[1]

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if (api_key is None):
        raise Exception("api_key could not be read")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

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


if __name__ == "__main__":
    main()
