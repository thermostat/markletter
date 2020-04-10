## Markletter

Markdown to LaTeX Letter conversion using pypandoc and jinja. See requirements.txt for 
python requirements. Extra-python requirements are pdflatex and pandoc.

    python build_letter.py example/yourbrain.md

To add a signature file (expected ~85 pixels height):

    python build_letter.py example/yourbrain.md --sig example/bob_sig.png

## Metadata

The `build_letter.py` script preprocesses the markdown file for
letter-specific metadata. For example, in the `yourbrain.md`
the beginning of the file specifies the following:

    %from: Bob
    %to_line: Heya Tom:
    %to_addr: Down the hall \\ Your Town, USA
    %from_addr: Just outside \\ 65212
    

The following metadata is used:

* **from**: The name of the author
* **to_addr**: Address of the recipient. Use LaTeX `\\` for newlines.
* **to_line**: Salutation. Defaults to `Dear sir or madam`. 
* **from_addr**: Sender address. Use LaTeX `\\` for newlines.
