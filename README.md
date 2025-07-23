Boot.dev project for mini ai agent

make sure to have UV installed by using the following command
⇒ curl -LsSf https://astral.sh/uv/install.sh | sh
and then doing the following steps to properly setup your environment
(MAKE SURE TO DO THE COMMANDS AT THE ROOT OF YOUR PROJECT, AKA the directory where the main.py file is located)
1. uv venv
2. source .venv/bin/activate
3. uv add google-genai==1.12.1
4. uv add python-dotenv==1.1.0
