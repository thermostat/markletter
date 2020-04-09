## Markletter

Markdown to LaTeX Letter conversion using pypandoc and jinja. See requirements.txt for 
python requirements. Extra-python requirements are pdflatex and pandoc.

    python build_letter.py example/yourbrain.md

To add a signature file (expected ~85 pixels height):

    python build_letter.py example/yourbrain.md --sig example/bob_sig.png

