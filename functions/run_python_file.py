import os
import config

def run_python_file(working_directory, file_path, args=[]):
    # get the working directory
    wrk_dir = os.path.abspath(working_directory)
    # get the file to be written to
    tgt_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    # get the directory the file is supposed to be located in
    tgt_path_dir = os.path.dirname(tgt_path_file)

    if (not tgt_path_file.startswith(wrk_dir)):
        return f'Error: Cannot execute "{tgt_path_file}" as it is outside the permitted working directory'
    
    if (not os.path.exists(tgt_path_file)):
        return f'Error: File "{tgt_path_file}" not found.'
    
    try:
        with open(tgt_path_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{tgt_path_file}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error reading file content {e}"
    
    