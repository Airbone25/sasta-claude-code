from langchain.tools import tool
from pathlib import Path

PROJECT_ROOT = Path("/workspaces/agent-langchain/creations")

def resolve_path(path: str) -> Path:
    target = (PROJECT_ROOT / path).resolve()

    if not target.is_relative_to(PROJECT_ROOT.resolve()):
        raise ValueError("Access denied")

    return target

@tool
def create_directory(folder_name: str) -> str:
    """Create a new directory inside the project.
    
    Creates parent directories if they do not exist.
    Does not fail if the directory already exists.
    """
    try:
        target = PROJECT_ROOT/folder_name
        print(f"Creating {folder_name}")
        target.mkdir(parents=True, exist_ok=True)

        return f"Successfully created directory: {folder_name}"
    except PermissionError:
        return "Permission denied: Cannot create directory."

@tool
def write_file(path: str, content: str) -> str:
    """Create or overwrite a file in the project."""
    target = PROJECT_ROOT/path

    print(f"Writing {path}")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

    return f"Successfully wrote {path}"

@tool
def read_file(path: str) -> str:
    """Read the contents of a file and return them."""
    target = resolve_path(path)

    print(f"Reading {path}")

    if not target.is_file():
        return "Error: File not found"

    try:
        if target.exists():
                text = target.read_text(encoding="utf-8")
                return f"Read {path} successful\n Content: {text}"
    except OSError as e:
        return f"Error reading files: {e}"

@tool
def list_files(path: str = ".") -> str:
    """List all files and directories inside a directory"""

    folder = resolve_path(path)

    if not folder.is_dir():
        return "Error: Directory not found"

    results = []

    for item in folder.iterdir():
        if item.is_dir():
            print(f"DIR: {item.name}")
            results.append(f"DIR: {item.name}")
        elif item.is_file():
            print(f"FILE: {item.name}")
            results.append(f"FILE: {item.name}")

    return "\n".join(results)


@tool
def edit_file(path: str, old_text: str, new_text: str) -> str:
    """Replace specific text in an existing file"""
    target = resolve_path(path)

    print(f"Editing {path}")

    content = target.read_text(encoding="utf-8")
    if content.count(old_text) == 1:
        content = content.replace(old_text,new_text,1)
        target.write_text(content, encoding="utf-8")
        return f"Successfully Editied {path}"
    else:
        return f"Old text was not present"

