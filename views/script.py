import base64
import re
import os

def extract_and_save_images(html_content, output_dir='images'):
    # Create directory for images if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find all Base64 encoded images
    base64_images = re.findall(r'data:image/(\w+);base64,([A-Za-z0-9+/=]+)', html_content)
    
    image_counter = 1  # To generate unique file names
    for img_format, base64_data in base64_images:
        # Generate file name for each image (e.g., image1.png)
        image_filename = f"image{image_counter}.{img_format}"
        image_path = os.path.join(output_dir, image_filename)

        # Decode the Base64 string and save it as a file
        with open(image_path, "wb") as img_file:
            img_file.write(base64.b64decode(base64_data))
        
        # Replace the Base64 string in HTML with the new image file path
        base64_string = f'data:image/{img_format};base64,{base64_data}'
        html_content = html_content.replace(base64_string, f'{output_dir}/{image_filename}')
        
        image_counter += 1

    return html_content

# Read the HTML file
input_html_file = 'menu.html'
with open(input_html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Call the function to extract images and update the HTML content
updated_html = extract_and_save_images(html_content)

# Write the updated HTML content to a new file
output_html_file = 'index_updated.html'
with open(output_html_file, 'w', encoding='utf-8') as file:
    file.write(updated_html)

print(f"Images extracted and HTML updated. Check '{output_html_file}' and the current folder.")
