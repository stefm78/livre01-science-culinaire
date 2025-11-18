#!/usr/bin/env python3
"""
Script d'optimisation images pour PAO : conversion 300dpi, mode couleur CMJN
Usage : python optimize-images.py
"""
import os
from PIL import Image

def optimize_image(in_path, out_path):
    img = Image.open(in_path)
    img = img.convert('CMYK')
    filename = os.path.splitext(os.path.basename(in_path))[0]
    # Redimensionner à résolution 300dpi si possible
    dpi = img.info.get('dpi', (72,72))[0]
    if dpi < 300:
        # Garder le format d'origine, appliquer 300dpi seulement
        img.save(out_path, dpi=(300,300))
    else:
        img.save(out_path)

# Répertoire source/destination
recette_src = '../../../recettes/'
schema_src = '../../../sources/schemas/'
recette_dst = '../02-assemblage/images-optimized/recettes/'
schema_dst = '../02-assemblage/images-optimized/schemas/'

os.makedirs(recette_dst, exist_ok=True)
os.makedirs(schema_dst, exist_ok=True)

# Recettes - images hero et process
for root, dirs, files in os.walk(recette_src):
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg'):
            if 'hero' in file or 'process' in file:
                in_f = os.path.join(root, file)
                out_f = os.path.join(recette_dst, file)
                optimize_image(in_f, out_f)

# Schémas scientifiques
for file in os.listdir(schema_src):
    if file.endswith('.png') or file.endswith('.jpg'):
        in_f = os.path.join(schema_src, file)
        out_f = os.path.join(schema_dst, file)
        optimize_image(in_f, out_f)
