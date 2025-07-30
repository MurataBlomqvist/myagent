import os
import config
from google.genai import types

def write_file(working_directory, file_path, content):
    # get the working directory
    wrk_dir = os.path.abspath(working_directory)
    # get the file to be written to
    tgt_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    # get the directory the file is supposed to be located in
    tgt_path_dir = os.path.dirname(tgt_path_file)

    if (not tgt_path_file.startswith(wrk_dir)):
        return f'Error: Cannot write to "{tgt_path_file}" as it is outside the permitted working directory'
    
    if (not os.path.exists(tgt_path_dir)):
        try:
            os.makedirs(tgt_path_dir)
        except Exception as e:
            return f"Error creating directory {e}"
    
    try:
        with open(tgt_path_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{tgt_path_file}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error reading file content {e}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="write_file",
    description="Replace t, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
