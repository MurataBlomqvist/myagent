import os


def get_files_info(working_directory, directory="."):
    #err_flg = True
    wrk_dir = os.path.abspath(working_directory)
    tgt_dir = os.path.abspath(os.path.join(working_directory, directory))

    if (not tgt_dir.startswith(wrk_dir)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if (not os.path.isdir(tgt_dir)):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_content = os.listdir(tgt_dir)
        str_contents = []
        for filename in dir_content:
            filepath = os.path.join(tgt_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            str_contents.append(f"- {filename}: file_size={file_size}, is_dir={is_dir}")
            #print()
        return "\n".join(str_contents)
    except Exception as e:
        return F"Error listing files {e}"
    
    
#def disp_content(err_flg, directory, print_tuple=("")):
#    print(f"Result for '{directory}' directory")
#    if (directory):

