import os
import re
import argparse
from collections import defaultdict

def find_python_files(directory):
    """Recursively find all .py files in the given directory and its subdirectories."""
    python_files = []
    for root, _, files in os.walk(directory):
        python_files.extend(
            os.path.join(root, file) for file in files if file.endswith('.py')
        )
    return python_files

def extract_arguments(file_path):
    """Extract --arguments from a Python file."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Updated regular expression to find add_argument calls including object.methodname syntax
    pattern = r'add_argument\s*\(\s*[\'"](-{1,2}[\w.-]+)[\'"]'
    
    arguments = re.findall(pattern, content)
    return set(arguments)  # Use a set to remove duplicates within the file

def parse_arguments_from_files(directory):
    """Parse arguments from all Python files in the directory and its subdirectories."""
    python_files = find_python_files(directory)
    all_arguments = defaultdict(set)
    
    for file_path in python_files:
        try:
            file_arguments = extract_arguments(file_path)
            for arg in file_arguments:
                all_arguments[arg].add(file_path)
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
    
    return all_arguments

def generate_add_arguments_function(all_arguments):
    """Generate the add_arguments function with all discovered arguments."""
    function_code = [
        "import argparse",
        "",
        "",
        "def get_arguments():",
        "    parser = argparse.ArgumentParser()",
        "    return add_arguments(parser)",
        "",
        "",
        "def add_arguments(parser):",
        "    # This function adds all discovered arguments to the parser",
        "    # It was automatically generated based on the project's Python files",
        ""
        
    ]
    
    for arg in sorted(all_arguments.keys()):
        # Strip leading dashes and replace remaining dashes with underscores for the dest parameter
        dest = arg.lstrip('-').replace('-', '_')
        function_code.append(f"    parser.add_argument('{arg}', dest='{dest}')")
    
    function_code.append("    return parser")
    return "\n".join(function_code)

def main():
    parser = argparse.ArgumentParser(description="Parse --arguments from Python files.")
    parser.add_argument("directory", help="Directory to search for Python files")
    args = parser.parse_args()

    all_arguments = parse_arguments_from_files(args.directory)

    print("Generating add_arguments function...")
    add_arguments_function = generate_add_arguments_function(all_arguments)
    
    # Write the function to a file
    with open("neurons/add_arguments.py", "w", encoding="utf-8") as f:
        f.write(add_arguments_function)
    
    print("add_arguments function has been written to add_arguments.py")
    
    print("\nUnique --arguments found:")
    for arg, files in sorted(all_arguments.items()):
        print(f"{arg}:")
        for file in sorted(files):
            print(f"  - {file}")
        print()

if __name__ == "__main__":
    main()