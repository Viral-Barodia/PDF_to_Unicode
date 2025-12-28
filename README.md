# PDF_to_Unicode

This repository contains scripts and datasets used to convert scanned PDF documents
into clean, Unicode-compliant text files using **Poppler** and **Tesseract OCR**.

The project was created while building **Gujarati and Telugu Unicode corpora**
from scanned copies of the Indian Constitution, and later analyzing their
phonetic and linguistic properties.

[Inference Article](https://medium.com/@barodia21/gujarati-and-telugu-a-compare-and-contrast-c2b61bb3a013)
[Kaggle Analysis Article](https://medium.com/@barodia21/gujarati-and-telugu-kaggle-analysis-319f91cce780)

---

## 🔧 Pipeline Overview

The conversion pipeline works in three stages:

### 1️⃣ PDF → Images (Poppler)
Scanned PDFs are first converted into high-resolution page images using **Poppler**.
This step ensures that OCR receives clean, readable inputs.

**Why Poppler?**
- Reliable PDF rendering
- High-quality image extraction
- Works well with multi-page scanned documents

---

### 2️⃣ Images → Unicode Text (Tesseract OCR)
The extracted images are passed to **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)**,
configured with language-specific trained models.

**Languages used:**
- Gujarati (`guj.traineddata`)
- Telugu (`tel.traineddata`)

The output is raw Unicode text containing OCR noise, page numbers,
headers, and non-script characters.

---

### 3️⃣ Unicode Cleaning & Normalization
Post-OCR cleaning scripts:

- Remove non-native Unicode characters
- Strip page numbers, headers, and formatting noise
- Preserve only language-specific Unicode blocks

This produces **analysis-ready `.txt` files** suitable for NLP, phonetic,
and statistical analysis.

---

## ✅ Ready-to-Use Datasets (Recommended)

If you only want the Unicode text, you **do not need to run any scripts**.

You can directly use the finalized text files:

- `guj_text.txt` — Gujarati Constitution (Unicode)  
- `tel_text.txt` — Telugu Constitution (Unicode)

These files are:

- OCR-processed  
- Cleaned to retain only native script characters  
- Suitable for linguistic analysis, NLP, or corpus studies

---

## ⚙️ Optional: Run the Full OCR Pipeline

If you want to generate the Unicode text yourself instead of using the pre-cleaned files, you can use the provided scripts with Tesseract and the trained data files.

**Steps:**

1. **Prepare the PDFs**  
   Place the scanned PDF files in the appropriate folder.

2. **Convert PDF → Images**  
   Use the Poppler-based script to convert each PDF page into a high-resolution image.

3. **OCR Images → Unicode Text**  
   Run the Tesseract OCR script with the respective trained data:

   - Gujarati: `guj.traineddata`  
   - Telugu: `tel.traineddata`

   Example command:

   ```bash
   tesseract page_image.png guj_text -l guj
