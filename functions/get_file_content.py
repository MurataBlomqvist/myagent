import os
import config
from google.genai import types

def get_file_content(working_directory, file_path):
    #err_flg = True
    wrk_dir = os.path.abspath(working_directory)
    tgt_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if (not tgt_file_path.startswith(wrk_dir)):
        return f'Error: Cannot read "{tgt_file_path}" as it is outside the permitted working directory'
    
    if (not os.path.isfile(tgt_file_path)):
        return f'Error: File not found or is not a regular file: "{tgt_file_path}"'
    
    try:
        rslt_str = ""
        with open(tgt_file_path, "r") as f:
            file_content_string = f.read()

            if (len(file_content_string) > config.MAX_CHAR):
                rslt_str = f"{file_content_string[:config.MAX_CHAR]}[...File {tgt_file_path} truncated at 10000"
            else:
                rslt_str = file_content_string
            return rslt_str

    except Exception as e:
        return f"Error reading file content {e}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the file content of a specific file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "file_name": types.Schema(
                type=types.Type.STRING,
                description="The file name to the specific file which its content shall be printed. If not provided, simply return (content not found)",
            )
        },
    ),
)