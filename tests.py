from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "main.py")
    print("Result for 'main' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg' file:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat' file:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist.py' directory:")
    print(result)


if __name__ == "__main__":
    test()