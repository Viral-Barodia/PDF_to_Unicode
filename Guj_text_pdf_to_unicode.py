# OCR_PDF_GujTel_Final.py

from pdf2image import convert_from_path
import pytesseract
import re
import os

# -------------------- CONFIG --------------------
# Poppler bin path (folder containing pdfinfo.exe)
poppler_path = r"D:\Personal_Projects\Projects\Guj_&_Tel\Release-25.11.0-0\poppler-25.11.0\Library\bin"

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# PDF paths
guj_pdf = r"D:\Personal_Projects\Projects\Guj_&_Tel\Constitution_Gujarati.pdf"
tel_pdf = r"D:\Personal_Projects\Projects\Guj_&_Tel\Constitution_Telugu.pdf"

# Output text files
guj_txt_file = "guj_text.txt"
tel_txt_file = "tel_text.txt"

# -------------------- FUNCTIONS --------------------
def clean_text(text):
    """Clean OCR text: remove extra spaces, page numbers, line breaks."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'Page\s*\d+', '', text)
    return text.strip()

def ocr_pdf_pagewise(pdf_path, lang_code):
    """OCR a PDF one page at a time to avoid memory issues."""
    from pdf2image.pdf2image import pdfinfo_from_path

    # Get total pages
    info = pdfinfo_from_path(pdf_path, poppler_path=poppler_path)
    total_pages = int(info["Pages"])
    print(f"Total pages in {pdf_path}: {total_pages}")

    # OCR text
    text = ""
    for page in range(1, total_pages + 1):
        print(f"OCR {pdf_path} - page {page}/{total_pages}")
        images = convert_from_path(
            pdf_path,
            dpi=200,               # Lower DPI to save memory
            poppler_path=poppler_path,
            first_page=page,
            last_page=page
        )
        page_img = images[0]
        page_text = pytesseract.image_to_string(
            page_img,
            lang=lang_code  # "guj" or "tel"
            # TESSDATA_PREFIX env variable must be set to Tesseract folder
        )
        text += page_text + "\n"

    return clean_text(text)

# -------------------- OCR PROCESS --------------------
# Gujarati OCR
print("Starting Gujarati OCR...")
guj_text = ocr_pdf_pagewise(guj_pdf, "guj")
with open(guj_txt_file, "w", encoding="utf-8") as f:
    f.write(guj_text)
print(f"Gujarati OCR complete → {guj_txt_file}")

# Telugu OCR
print("Starting Telugu OCR...")
tel_text = ocr_pdf_pagewise(tel_pdf, "tel")
with open(tel_txt_file, "w", encoding="utf-8") as f:
    f.write(tel_text)
print(f"Telugu OCR complete → {tel_txt_file}")
