import os
import config
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    args = {
        "working_directory": "./calculator"
        , 
    }
    #print(function_call_part.args)
    for value in function_call_part.args:
        args[value] = function_call_part.args[value]
    
    func_dict = {
        "get_files_info": get_files_info
        , "get_file_content": get_file_content
        , "run_python_file": run_python_file
        , "write_file": write_file
    }

    if function_call_part.name not in func_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    func_res = func_dict[function_call_part.name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": func_res},
            )
        ],
    )