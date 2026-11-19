from langchain.tools import tool
from pathlib import Path

PROJECT_ROOT = Path("/workspaces/agent-langchain/creations")

#Create Directories

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

