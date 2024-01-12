import os
import time
def get_valid_dir():
    directory_path = input("Directory: ")
    if os.path.isdir(directory_path):
        return directory_path
    else:
        print("Invalid directory.")

def rename_files(dir_path, log_file):
    initial_dir = os.path.abspath(dir_path)
    
    for root, dirs, files in os.walk(dir_path):
        current_folder_name = os.path.basename(root)

        # Get the parent folder of current_folder_name
        parent_folder_path = os.path.dirname(root)
        name = os.path.basename(parent_folder_path)

        counter = 0
        rel_path = os.path.relpath(root, initial_dir)
        # Fail Safe
        if rel_path != ".":
            print(f"\n Renaming {rel_path}")
            log_file.write(f"********Renaming {rel_path}********\n")
            
        for file in files:
            counter += 1
            old_file = os.path.join(root, file)
            file_ext = os.path.splitext(old_file)[1]                
            if counter < 10:
                new_name = f"{name}_{current_folder_name}_0{counter}{file_ext}"
            else:
                new_name = f"{name}_{current_folder_name}_{counter}{file_ext}"

            new_file = os.path.join(root, new_name)

            # Fail Safe: making sure we don't make a file out of the log file we created
            if "rename_log.txt" not in old_file:
                try:
                    os.rename(old_file, new_file)
                    log_file.write(f"* Renamed: {file} to {new_name}\n")
                except FileExistsError as e:
                    print(f"Skipping file {old_file}, it already exists.")
                except Exception as e:
                    print(f"{e}")
                    raise

        counter = 0  # Reset counter for each subdirectory


def main():
    while True:
        try:
            exit_code = input("\n[Enter] to continue, 'exit' to quit. \n")
            if exit_code.lower() == 'exit':
                print("Thank you... Goodbye.")
                break
            else:
                directory_path = get_valid_dir()
                
                log_file_path = os.path.join(directory_path, "rename_log.txt")
                if os.path.exists(log_file_path):
                    os.remove(log_file_path)
                
                with open(log_file_path, 'a') as log_file:
                    rename_files(directory_path, log_file)
        except KeyboardInterrupt as e:
            print("User exited. Quitting in 3s...Please wait.")
            time.sleep(3)
            exit()

if __name__ == "__main__":
    main()
