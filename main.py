from PIL import Image
from pathlib import Path

# Define the base directory
base_path = Path.home() / "Dropbox" / "Marketing" / "Webflow Images" / "Product Guide"

# Define the input and output directories using the base directory
path = base_path
pathOut = base_path / "Compressed"
size = (2400, 1600)

# Ensure the output directory exists
pathOut.mkdir(parents=True, exist_ok=True)

for file_path in path.iterdir():
    # Check if it's a file and not '.DS_Store'
    if file_path.is_file() and file_path.name != ".DS_Store":
        img = Image.open(file_path)

        # Resizing using LANCZOS for highest quality
        edit = img.resize(size, resample=1, reducing_gap=3.0)

        clean_name = file_path.stem
        (pathOut / f"{clean_name}_edited.jpg").save(edit, quality=100, optimize=True)
