# OCR_Telugu_MemorySafe.py

from pdf2image import convert_from_path
import pytesseract
import os
import gc

# -------------------- CONFIG --------------------
# Poppler bin path (folder containing pdfinfo.exe)
poppler_path = r"D:\Personal_Projects\Projects\Guj_&_Tel\Release-25.11.0-0\poppler-25.11.0\Library\bin"

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# PDF path
tel_pdf = r"D:\Personal_Projects\Projects\Guj_&_Tel\Constitution_Telugu.pdf"

# Output text file
tel_txt_file = r"D:\Personal_Projects\Projects\Guj_&_Tel\tel_text.txt"

# Temporary folder for Tesseract / PIL
temp_folder = r"D:\TempOCR"
os.makedirs(temp_folder, exist_ok=True)
os.environ["TMP"] = temp_folder
os.environ["TEMP"] = temp_folder
os.environ["TMPDIR"] = temp_folder

# -------------------- FUNCTIONS --------------------
def clean_text(text):
    """Clean OCR text: remove extra spaces, page numbers, line breaks."""
    import re
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'Page\s*\d+', '', text)
    return text.strip()

def ocr_pdf_pagewise(pdf_path, lang_code, output_file):
    """OCR a PDF one page at a time and write directly to file."""
    from pdf2image.pdf2image import pdfinfo_from_path

    # Get total pages
    info = pdfinfo_from_path(pdf_path, poppler_path=poppler_path)
    total_pages = int(info["Pages"])
    print(f"Total pages in {pdf_path}: {total_pages}")

    # Open output file
    with open(output_file, "w", encoding="utf-8") as f:
        for page in range(1, total_pages + 1):
            print(f"OCR {pdf_path} - page {page}/{total_pages}")
            # Convert single page to image
            images = convert_from_path(
                pdf_path,
                dpi=150,  # lower DPI to save memory
                poppler_path=poppler_path,
                first_page=page,
                last_page=page
            )
            page_img = images[0]

            # OCR using Tesseract
            page_text = pytesseract.image_to_string(
                page_img,
                lang=lang_code  # "tel" for Telugu
            )

            # Clean and write
            f.write(clean_text(page_text) + "\n")

            # Free memory
            del page_img
            del images
            gc.collect()

# -------------------- OCR PROCESS --------------------
print("Starting Telugu OCR...")
ocr_pdf_pagewise(tel_pdf, "tel", tel_txt_file)
print(f"Telugu OCR complete → {tel_txt_file}")
