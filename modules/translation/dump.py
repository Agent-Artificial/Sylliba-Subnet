import os
import base64

def dump_file(folder_path, file_name):
    # Construct full file path
    full_path = os.path.join(folder_path, file_name)
    
    # Ensure the file exists before proceeding
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"The file {full_path} does not exist.")
    
    # Read the content of the file
    with open(full_path, 'rb') as f:
        file_content = f.read()

    # Base64 encode the file content
    encoded_content = base64.b64encode(file_content)

    # Create the new file path for the dump file
    dump_file_name = f"{file_name}_dump.txt"
    dump_full_path = os.path.join(folder_path, dump_file_name)

    # Write the encoded content to the dump file
    with open(dump_full_path, 'wb') as dump_file:
        dump_file.write(encoded_content)

    print(f"Dumped encoded content to: {dump_full_path}")

# Example usage
folder_path = 'modules/translation'
file_name = 'install_translation.sh'

dump_file(folder_path, file_name)
