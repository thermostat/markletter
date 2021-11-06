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

## Requirements

See the Dockerfile, work in progress.

## History

Notes

   0 ls /usr/local
   1 ls /usr/local/share
   2 texlive
   3 tlshell
   4 ls /
   5 ls /usr
   6 ls /usr/local
   7 ls /usr/bin
   8 ls
   9 printenv
  10 ls /opt
  11 ls /opt/texlive/
  12 ls /opt/texlive/texdir/
  13 ls /opt/texlive/texdir/texmf-dist/
  14 ls /opt/texlive/texdir/texmf-dist/tex
  15 ls /home
  16 ls /opt/texlive/
  17 ls /opt/texlive/texmf-local/
  18 ls
  19 cd marketter
  20 cd /markletter
  21 ls
  22 cp -r footmisc/ /opt/texlive/texmf-local
  23 python3 build_letter.py example/yourbrain.md
  24 ls /opt/texlive/
  25 ls /opt/texlive/texmf-local/
  26 ls /opt/texlive/texmf-local/tlpkg/
  27 mv /opt/texlive/texmf-local/footmisc/ /opt/texlive/texmf-local/tlpkg/
  28 python3 build_letter.py example/yourbrain.md
  29 ls
  30 ls /opt/texlive
  31 ls /opt/texlive/texmf-local/
  32 ls
  33 cd footmisc/
  34 ls
  35 latex footmisc.ins
  36 ls
  37 latex footmisc.dtx
  38 ls
  39 cp footmisc.sty /opt/texlive/texmf-local/
  40 cd ..
  41 python3 build_letter.py example/yourbrain.md
  42 cp footmisc/footmisc.sty /opt/texlive/texmf-local/tlpkg/
  43 python3 build_letter.py example/yourbrain.md
  44 cp footmisc/footmisc.sty /opt/texlive/texmf-local/tex/
  45 python3 build_letter.py example/yourbrain.md
  46 cp footmisc/footmisc.sty /opt/texlive/texmf-local/footmisc/
  47 cp footmisc/footmisc.sty /opt/texlive/texmf-local/footmisc/footmisc.sty
  48 mkdir /opt/texlive/texmf-local/footmisc/
  49 cp footmisc/footmisc.sty /opt/texlive/texmf-local/footmisc/footmisc.sty
  50 python3 build_letter.py example/yourbrain.md
  51 mkdir /opt/texlive/texdir/texmf-dist/tex/footmisc
  52 cp footmisc/footmisc.sty /opt/texlive/texdir/texmf-dist/tex/footmisc/
  53 python3 build_letter.py example/yourbrain.md
  54 rm -rf /opt/texlive/texdir/texmf-dist/tex/footmisc
  55 cp footmisc/footmisc.sty /opt/texlive/texdir/texmf-dist/tex/
  56 python3 build_letter.py example/yourbrain.md
  57 cp footmisc/footmisc.sty /opt/texlive/texdir/texmf-dist/tex/latex/base/
  58 python3 build_letter.py example/yourbrain.md
  59 ls
  60 ls /opt/texlive/
  61 ls /opt/texlive/texdir
  62 ls /opt/texlive/texmf-local/
  63 cat /opt/texlive/texmf-local/ls-R
  64 pico
  65 kpsewhich footmisc
  66 kpsewhich -expand-var '$TEXMFHOME'
  67 ls /root/texmf
  68 kpsewhich -expand-var '$TEXMFLOCAL'
  69 mktexlsr
  70 python3 build_letter.py example/yourbrain.md
  71 history
