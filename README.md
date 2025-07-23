Boot.dev project for mini ai agent

make sure to have UV installed by using the following command
⇒ curl -LsSf https://astral.sh/uv/install.sh | sh
and then doing the following steps to properly setup your environment
(MAKE SURE TO DO THE COMMANDS AT THE ROOT OF YOUR PROJECT, AKA the directory where the main.py file is located)
1. uv venv
2. source .venv/bin/activate
3. uv add google-genai==1.12.1
4. uv add python-dotenv==1.1.0

after the installation of dependencies make sure to insert your own google gemini api key
1. in the root folder create a new file called .env
2. paste your own api key with the following format
   GEMINI_API_KEY="{paste your key here}"
3. paste the desired model name with the following format
    (in this tutorial we are using gemini flash model)
   GEMINI_MODEL_NAME="{paste your key here}"
   Example:
    GEMINI_MODEL_NAME="gemini-2.0-flash-001"