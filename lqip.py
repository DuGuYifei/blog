import os
from PIL import Image
import base64
from io import BytesIO

# Function to generate LQIP from image path
def generate_lqip(image_path):
    try:
        with Image.open(image_path) as img:
            img_small = img.resize((20, 12))
            buffer = BytesIO()
            img_small.save(buffer, format="WEBP", quality=30)
            base64_data = base64.b64encode(buffer.getvalue()).decode()
            return f'data:image/webp;base64,{base64_data}'
    except Exception as e:
        print(f"Error generating LQIP for {image_path}: {e}")
        return None

# Set your target folder here
target_folder = "./posts"
updated_files = []

# Recursively walk through the directory
for root, _, files in os.walk(target_folder):
    for filename in files:
        if filename.endswith(".md"):
            full_path = os.path.join(root, filename)
            print(f"Processing: {full_path}")

            with open(full_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Detect front matter boundaries
            if lines and lines[0].strip() == "---":
                try:
                    end_index = -1
                    for i, line in enumerate(lines):
                        if i == 0:
                            continue
                        if line.strip() == "---":
                            end_index = i
                            break
                except ValueError:
                    continue  # skip malformed files

                if end_index == -1:
                    continue  # no closing '---'

                front_matter = lines[0:end_index+1]
                body = lines[end_index+1:]

                has_image = any("image:" in line for line in front_matter)
                has_lqip = any("lqip:" in line for line in front_matter)
                if has_image and not has_lqip:
                    path_line = next((line for line in front_matter if "path:" in line), None)
                    if path_line:
                        image_path = path_line.split("path:")[-1].strip()
                        local_image_path = os.path.normpath(os.path.join(root, "..", image_path))

                        if os.path.exists(local_image_path):
                            lqip = generate_lqip(local_image_path)
                            if lqip:
                                insert_index = front_matter.index(path_line) + 1
                                front_matter.insert(insert_index, f' lqip: {lqip}\n')

                                with open(full_path, "w", encoding="utf-8") as file:
                                    file.writelines(front_matter + body)
                                updated_files.append(full_path)

print(f"Updated files: {updated_files}")
