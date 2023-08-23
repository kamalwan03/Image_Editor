from PIL import Image
import os

path = os.path.expanduser(
    "~/Dropbox/Marketing/Webflow Images/Product Guide"
)  # folder for unedited images
pathOut = os.path.expanduser(
    "~/Dropbox/Marketing/Webflow Images/Product Guide/Compressed"
)  # folder for edited images
size = (2400, 1600)

# Ensure the output directory exists
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    full_path = os.path.join(path, filename)

    # Check if it's a file and not '.DS_Store'
    if os.path.isfile(full_path) and filename != ".DS_Store":
        img = Image.open(full_path)

        # Resizing using LANCZOS for highest quality
        edit = img.resize(size, resample=1, reducing_gap=3.0)

        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{pathOut}/{clean_name}_edited.jpg", quality=100, optimize=True)
