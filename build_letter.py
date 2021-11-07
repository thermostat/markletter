#!/usr/bin/python3

###########################################################################
# Imports; see requirements.txt
###########################################################################

import jinja2
import pypandoc
import argparse
import os, copy
import tempfile, shutil

###########################################################################
# Defaults set by metadata
###########################################################################
DEFAULTS = {
    'to_addr' : 'The world',
    'to_line' : 'Dear sir or madam:',
    'sig_image' : None,
    'single_space' : False,
    'from' : os.environ.get('USER', 'User'),
    'closing' : 'Sincerly,',
    'body' : """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
}


###########################################################################
# Static Jinja setup
###########################################################################
latex_jinja_env = jinja2.Environment(
    block_start_string = r'\BLOCK{',
    block_end_string = '}',
    variable_start_string = r'\VAR{',
    variable_end_string = '}',
    loader=jinja2.FileSystemLoader(os.path.abspath('.')),
)

###########################################################################
# Functions
###########################################################################
def get_md_data(fname):
    """
    Preprocess step for letter metadata
    """
    fd = open(fname, 'r')
    meta = {}
    markdown_lines = []
    meta_done = False
    for line in fd:
        if line.startswith('%') and meta_done == False:
            k,v = line.strip()[1:].split(':', 1)
            meta[k] = v
        elif meta_done == False:
            meta_done = True
        if meta_done:
            markdown_lines.append(line.strip())
    return meta, '\n'.join(markdown_lines)

def decompose_path(fname):
    """
    Take a name like, /foo/blah/bar.ext
    into (/foo/bar, bar, ext)
    """
    path, fn = os.path.split(fname)
    name, ext = os.path.splitext(fn)
    return (path, name, ext)

def new_ext(fname, newext):
    path,name,ext = decompose_path(fname)
    if path == '':
        path = '.'
    return "{}/{}.{}".format(path, name, newext)

def get_tex_name(fname):
    return new_ext(fname, 'tex')

def get_pdf_name(fname):
    return new_ext(fname, 'pdf')

def run(fname, outdir):
    """
    Setup the files and invoke pdflatex
    """
    startdir = os.getcwd()
    tdir = None
    try:
        tdir = tempfile.TemporaryDirectory(prefix='mkl')
        shutil.copy(fname, tdir.name)
        os.chdir(tdir.name)
        args = copy.copy(DEFAULTS)
        file_metadata, markdown_strn = get_md_data(fname)
        args.update(file_metadata)
        latex_strn = pypandoc.convert_text(markdown_strn, 'latex', format='md')
        tex_name = get_tex_name(fname)
        args['body'] = latex_strn
        create_latex(args, tex_name)
        invoke_pdflatex(tex_name)
        pdf_name = os.path.basename(get_pdf_name(fname))
        print("PDF: {}".format(pdf_name))
        os.listdir('.')
        shutil.copy(pdf_name, outdir)
    finally:
        if tdir != None:
            shutil.rmtree(tdir.name)

def invoke_pdflatex(tex_name):
    os.system('pdflatex {}'.format(tex_name))

def create_latex(args, outname=None):
    templ = latex_jinja_env.get_template('latex_letter_template.in.tex')
    outdata = templ.render(**args)
    if outname:
        fd = open(outname, 'w')
        fd.write(outdata)
        fd.close()
    else:
        print(outdata)

def gen_args():
    parser = argparse.ArgumentParser(description="Markdown to LaTeX letter")
    parser.add_argument('file',
                        help='Input markdown file')
    parser.add_argument('--sig',
                        default=None,
                        help='Signature image file [85 px tall]')
    parser.add_argument('--outdir',
                        default=os.getcwd(),
                        help='output directory')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    import sys
    args = gen_args()
    if args.sig:
        DEFAULTS['sig_image'] = args.sig
    run(args.file, args.outdir)

    
