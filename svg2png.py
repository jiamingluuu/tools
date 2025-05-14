# convert svg to png

import os

import cairosvg

# get all svg files in the current directory
svg_files = [f for f in os.listdir(".") if f.endswith(".svg")]
for svg_file in svg_files:
    # convert svg to png
    cairosvg.svg2png(url=svg_file, write_to=svg_file.replace(".svg", ".png"))
