import os
import config
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # get the working directory
    wrk_dir = os.path.abspath(working_directory)
    # get the file to be written to
    tgt_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    # get the directory the file is supposed to be located in
    tgt_path_dir = os.path.dirname(tgt_path_file)

    if (not tgt_path_file.startswith(wrk_dir)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if (not os.path.exists(tgt_path_file)):
        return f'Error: File "{file_path}" not found.'
    
    if (tgt_path_file[len(tgt_path_file)-3:] != ".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        wrk_args = ["python", tgt_path_file]
        for arg in args:
            wrk_args.append(arg)
        
        completed_prc = subprocess.run(wrk_args, timeout=30, capture_output=True, cwd=wrk_dir)
        formatted_out = ""

        if (completed_prc.stdout != None):
            formatted_out += f"STDOUT:{completed_prc.stdout}\n"
        
        if (completed_prc.stderr != None):
            formatted_out += f"STDERR:{completed_prc.stderr}\n"

        if (completed_prc.returncode != 0):
            formatted_out += f"Process exited with code {completed_prc.returncode}\n"

        if (formatted_out == ""):
            formatted_out = "No output produced."
        
        return formatted_out
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    