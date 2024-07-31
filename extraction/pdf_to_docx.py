from pdf2image import convert_from_path
import os
from img_to_text import convert_image_to_docx

GENERATE_IMAGES = False

image_dir = f'extraction/output/pdf_images/'  # Replace with the path to your image directory
extract_dir = f'extraction/output/extracted_texts/'


os.makedirs(image_dir, exist_ok=True)
os.makedirs(extract_dir, exist_ok=True)

# Path to the PDF file you want to extract text from


pdf_file = r'C:\Users\david\OneDrive\Documents\GitHub\Digitizing-Govett\extraction\pdfs\The Apocalypse Expounded by Scripture - Robert Govett.pdf'

images = []

if GENERATE_IMAGES:
    # Convert PDF to images
    # for pdf_file in pdf_files:
    convert_from_path(pdf_file, output_folder=image_dir, fmt='png', poppler_path='C:\\Program Files\\Poppler\\Library\\bin')

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(root, file)
            images.append(image_path)

images.sort()

# Initialize an empty string to store the extracted text
extracted_text = ''

os.makedirs(extract_dir, exist_ok=True)

# Loop through each image and extract text
for i, image in enumerate(images):
    output_file = f'{extract_dir}/extracted_text-{i+1}.docx'

    if os.path.exists(output_file):
        print(f"{i + 1}/{len(images)} Already exists.")
        continue

    # Use pytesseract to extract text from the image
    convert_image_to_docx(image, output_file, prioritize_block_order_over_formatting=True)  

    # Print progress updates
    print(f"{i + 1}/{len(images)} Extracted text from page")

