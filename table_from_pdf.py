import os.path

import camelot

current_dir = os.getcwd()
pdf_file = 'code-complete-2nd-edition-v413hav.pdf'
file_path = os.path.join(current_dir, pdf_file)

tables = camelot.read_pdf(file_path,
                 pages="34")

tables.export('foo.csv',
              f='csv',
              compress=True)
tables[0].to_csv('foo.csv')