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
        return None

# Scan all markdown files in the current directory
updated_files = []

for filename in os.listdir():
    if filename.endswith(".md"):
        print(f"Found markdown file: {filename}")
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Detect front matter boundaries
        if lines[0].strip() == "---":
            print("Found front matter")
            try:
                end_index = -1
                for i, line in enumerate(lines):
                    if i == 0:
                        continue
                    if line.strip() == "---":
                        end_index = i
                        break
                print(f"Front matter ends at line {end_index}")
            except ValueError:
                continue  # skip malformed files

            front_matter = lines[0:end_index+1]
            body = lines[end_index+1:]

            has_image = any("image:" in line for line in front_matter)
            has_lqip = any("lqip:" in line for line in front_matter)
            print(f"has_image: {has_image}, has_lqip: {has_lqip}")
            if has_image and not has_lqip:
                print("Image found, but no LQIP")
                # Try to find image path
                path_line = next((line for line in front_matter if "path:" in line), None)
                if path_line:
                    image_path = path_line.split("path:")[-1].strip()
                    local_image_path = f"../{image_path}"  # Assuming relative to project root

                    if os.path.exists(local_image_path):
                        lqip = generate_lqip(local_image_path)
                        if lqip:
                            # Find where to insert the lqip line
                            insert_index = front_matter.index(path_line) + 1
                            front_matter.insert(insert_index, f' lqip: {lqip}\n')

                            # Write back the modified file
                            with open(filename, "w", encoding="utf-8") as file:
                                file.writelines(front_matter + body)
                            updated_files.append(filename)
