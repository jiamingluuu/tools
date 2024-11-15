import os
import sys
from PyPDF2 import PdfReader


def extract_text_from_pdfs(directory):


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_pdf_text.py <directory>")

    directory = sys.argv[1]
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    for filename in pdf_files:
        pdf_path = os.path.join(directory, filename)
        try:
            reader = PdfReader(pdf_path)
            text = ''
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            # Write the extracted text to a .txt file
            base_filename = os.path.splitext(filename)[0]
            txt_filename = base_filename + '.txt'
            txt_path = os.path.join(directory, txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Extracted text from '{filename}' to '{txt_filename}'.")
        except Exception as e:
            print(f"Error processing '{filename}': {e}")

