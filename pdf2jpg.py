# Split PDF file into pages, store as JPG files
# Get the PDF file by dragging it onto the script

# from progress.bar import Bar
import os
import sys
from os.path import dirname, join
from textwrap import fill

from pdf2image import convert_from_path

# Path to PDF file
pdf_path = sys.argv[1]
# pdf_path = r"C:\Users\15149\OneDrive - University of Toronto\UTSC\2022\2022 - FALL\MATB41\ASSIGNMENTS\A9\MATB41-A9.pdf"
# pdf_path = join(dirname(__file__), 'in.pdf')

# Convert PDF to JPG
print("Converting PDF to JPG...")


# Create a generator for the output filename
def gen_filename():
    while True:
        yield os.path.splitext(os.path.basename(pdf_path))[0]


# Convert PDF to JPG
jpg_folder = join(dirname(pdf_path), "JPG")

# Create a folder for the JPG files
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# image = convert_from_path(pdf_path)
convert_from_path(
    pdf_path,
    dpi=500,
    thread_count=16,
    output_folder=jpg_folder,
    output_file=gen_filename(),
    # output_file= os.path.splitext(os.path.basename(pdf_path))[0],
    fmt="jpeg",
    jpegopt={"quality": 100},
)
print("Done")

# # Create JPG foler
# jpg_folder = join(dirname(pdf_path), 'JPG')
# if not os.path.exists(jpg_folder):
#     os.makedirs(jpg_folder)

# # Save JPG files
# with Bar('Saving JPG files...', max=len(images), fill = '▪') as bar: # ⬛⬜◼▪▫
#     for i, image in enumerate(images):
#         # print ('Saving page %d...' % (i+1))
#         image.save(join(jpg_folder, 'page_%d.jpg' % (i+1)))
#         bar.next()
