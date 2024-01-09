import os


def get_valid_dir():
    directory_path = input("Directory: ")
    if os.path.isdir(directory_path):
        return directory_path
    else:
        print("Invalid directory.")

def rename_files(dir_path, name, season, file_ext):
    files = os.listdir(dir_path)


    counter = 0
    for file in files:
        counter += 1
        if counter < 10:
            new_name = f"{name}_{season}_0{counter}.{file_ext}"
        else:
            new_name = f"{name}_{season}_{counter}.{file_ext}"
        
        old_file = os.path.join(dir_path, file)
        new_file = os.path.join(dir_path, new_name)
        
        try:
            os.rename(old_file, new_file)
        except FileExistsError as e:
            print(f"Skipping file {old_file}, it already exist.")
        except Exception as e:
            print("Unknown error, goodbye.")

file_ext = input("file extension: ")
while True:
    exit_code = input("\n[Enter] to continue, 'exit' to quit. ")
    if exit_code.lower() == 'exit':
        print("Thank you... Goodbye.")
    else:
        directory_path = get_valid_dir()
        name = input("Name: ")
        season = input("Season: ")
    
        rename_files(directory_path, name, season, file_ext)
